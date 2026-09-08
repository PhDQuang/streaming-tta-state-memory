"""Export the reviewed Markdown manuscript to reproducible LuaLaTeX source.

Uses only the Python standard library. This is a deliberately strict converter
for this manuscript's headings, paragraphs, emphasis, links, tables and images;
unsupported block syntax fails rather than silently losing content. Run after
scripts/build_paper.py. No TeX engine is invoked and no PDF is claimed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re


ROOT=Path(__file__).resolve().parents[1]
TOKEN=re.compile(r"(`[^`\n]+`|\*\*[^*\n]+\*\*|\[[^\]\n]+\]\([^\s)]+\))")
IMAGE=re.compile(r"!\[([^\]]*)\]\(([^\s)]+)\)\Z")
HEADING=re.compile(r"(#{1,6})\s+(.+)\Z")
CAPTION=re.compile(r"(?:Table|Figure)\s*\d+\.\s*(.+)\Z")
SPECIAL={"\\":r"\textbackslash{}","&":r"\&","%":r"\%","$":r"\$","#":r"\#",
         "_":r"\_","{":r"\{","}":r"\}","~":r"\textasciitilde{}","^":r"\textasciicircum{}",
         "±":r"\ensuremath{\pm}","−":r"\ensuremath{-}","×":r"\ensuremath{\times}",
         "≤":r"\ensuremath{\leq}","≥":r"\ensuremath{\geq}"}


def escape(text):
    return "".join(SPECIAL.get(char,char) for char in text)


def relative_target(target,source,output):
    if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:",target) or target.startswith("#"):
        return target
    return Path(os.path.relpath((source.parent/target).resolve(),output.parent.resolve())).as_posix()


def inline(text,source,output):
    pieces=[]
    for token in TOKEN.split(text):
        if token.startswith("`") and token.endswith("`"):
            pieces.append(r"\texttt{"+escape(token[1:-1])+"}")
        elif token.startswith("**") and token.endswith("**"):
            pieces.append(r"\textbf{"+inline(token[2:-2],source,output)+"}")
        elif token.startswith("[") and "](" in token:
            label,target=token[1:-1].split("](",1)
            target=relative_target(target,source,output)
            if any(char in target for char in "{}\\\n\r"):
                raise ValueError(f"Unsupported hyperlink target: {target}")
            # TeX lexical special characters must be escaped even inside href.
            url=target.replace("%",r"\%").replace("#",r"\#").replace("&",r"\&").replace("_",r"\_")
            pieces.append(r"\href{"+url+"}{"+escape(label)+"}")
        else:
            if "**" in token or "`" in token or re.search(r"!?\[[^\]]*\]\(",token):
                raise ValueError(f"Unsupported or unbalanced inline Markdown: {token}")
            pieces.append(escape(token))
    return "".join(pieces)


def table_cells(line):
    if not line.startswith("|") or not line.endswith("|"):
        raise ValueError("Table rows require explicit outer pipes")
    return [cell.strip() for cell in line[1:-1].split("|")]


def following_caption(lines,start,kind):
    position=start
    while position<len(lines) and not lines[position].strip():
        position+=1
    if position<len(lines) and lines[position].startswith(kind):
        match=CAPTION.fullmatch(lines[position])
        if match:
            return match.group(1),position+1
    raise ValueError(f"Every {kind.lower()} requires its source Markdown caption")


def convert(source,output):
    raw=source.read_bytes()
    lines=raw.decode("utf-8-sig").splitlines()
    titles=[line[2:].strip() for line in lines if line.startswith("# ")]
    if len(titles)!=1:
        raise ValueError("Expected exactly one manuscript title")
    counts={"headings":0,"tables":0,"figures":0,"paragraphs":0}
    assets=[]
    body=[]
    position=0
    while position<len(lines):
        line=lines[position].strip()
        if not line:
            position+=1
            continue
        heading=HEADING.fullmatch(line)
        if heading:
            depth=len(heading.group(1))
            counts["headings"]+=1
            if depth>1:
                command={2:"section",3:"subsection",4:"subsubsection",5:"paragraph",6:"subparagraph"}[depth]
                body.append("\\"+command+"*{"+inline(heading.group(2),source,output)+"}\n")
            position+=1
            continue
        image=IMAGE.fullmatch(line)
        if image:
            alt,target=image.groups()
            asset=(source.parent/target).resolve()
            if not asset.is_file():
                raise FileNotFoundError(f"Manuscript figure is missing: {asset}")
            target=relative_target(target,source,output)
            if any(char in target for char in "{}%#\\\n\r"):
                raise ValueError(f"Unsupported figure path: {target}")
            caption,position=following_caption(lines,position+1,"Figure")
            counts["figures"]+=1
            assets.append({"path":target,"sha256":hashlib.sha256(asset.read_bytes()).hexdigest()})
            body.append("% Source figure alt text: "+alt.replace("\n"," ")+"\n"+
                "\\begin{figure}[htbp]\n\\centering\n"+
                r"\includegraphics[width=\linewidth,height=.65\textheight,keepaspectratio]{\detokenize{"+target+"}}\n"+
                r"\caption{"+inline(caption,source,output)+"}\n"+
                r"\label{fig:recorded-"+str(counts["figures"])+"}\n\\end{figure}\n")
            continue
        if line.startswith("|"):
            rows=[]
            while position<len(lines) and lines[position].strip().startswith("|"):
                rows.append(table_cells(lines[position].strip()))
                position+=1
            width=len(rows[0])
            if len(rows)<3 or width<2 or any(len(row)!=width for row in rows):
                raise ValueError("Invalid or ragged Markdown table")
            if not all(re.fullmatch(r":?-{3,}:?",cell) for cell in rows[1]):
                raise ValueError("Missing Markdown table header separator")
            caption,position=following_caption(lines,position,"Table")
            counts["tables"]+=1
            columns=r"@{}>{\raggedright\arraybackslash}X"+r">{\centering\arraybackslash}X"*(width-1)+"@{}"
            result=[r"\begin{table}[htbp]",r"\centering\small",r"\setlength{\tabcolsep}{3pt}",
                    r"\begin{tabularx}{\linewidth}{"+columns+"}",r"\toprule"]
            for i,row in enumerate([rows[0],*rows[2:]]):
                result.append(" & ".join(inline(cell,source,output) for cell in row)+r" \\")
                if i==0:
                    result.append(r"\midrule")
            result.extend([r"\bottomrule",r"\end{tabularx}",r"\caption{"+inline(caption,source,output)+"}",
                           r"\label{tab:recorded-"+str(counts["tables"])+"}",r"\end{table}"])
            body.append("\n".join(result)+"\n")
            continue
        if re.match(r"(?:```|~~~|>|[-*+]\s|\d+\.\s|<)",line):
            raise ValueError(f"Unsupported manuscript block syntax at line {position+1}: {line[:80]}")
        paragraph=[line]
        position+=1
        while position<len(lines) and lines[position].strip():
            next_line=lines[position].strip()
            if HEADING.fullmatch(next_line) or IMAGE.fullmatch(next_line) or next_line.startswith("|"):
                break
            paragraph.append(next_line)
            position+=1
        counts["paragraphs"]+=1
        body.append(inline(" ".join(paragraph),source,output)+"\n")
    source_hash=hashlib.sha256(raw).hexdigest()
    exporter_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    preamble=("% Generated by scripts/export_latex.py; edit the Markdown source, then rerun.\n"
              "% Requires LuaLaTeX. Compilation has not been performed or claimed.\n"
              "% From the paper directory: lualatex paper.tex (twice for references).\n"
              "% Markdown SHA256: "+source_hash+"\n% Exporter SHA256: "+exporter_hash+"\n"+
              "% Structure: "+json.dumps(counts,sort_keys=True)+"\n"+
              """\\documentclass[11pt]{article}
\\usepackage[a4paper,margin=25mm]{geometry}
\\usepackage{iftex}
\\ifLuaTeX\\else\\errmessage{This Unicode manuscript requires LuaLaTeX}\\fi
\\usepackage{fontspec}
\\setmainfont{Latin Modern Roman}
\\setsansfont{Latin Modern Sans}
\\setmonofont{Latin Modern Mono}
\\usepackage{microtype}
\\usepackage{array,booktabs,longtable,tabularx}
\\usepackage{graphicx}
\\usepackage{hyperref}
\\hypersetup{colorlinks=true,urlcolor=blue,linkcolor=blue,unicode=true}
\\urlstyle{same}
\\setlength{\\emergencystretch}{3em}
\\setlength{\\parindent}{0pt}
\\setlength{\\parskip}{.55em}
"""+r"\title{"+escape(titles[0])+"}\n\\author{}\n\\date{}\n\\begin{document}\n\\maketitle\n")
    tex=preamble+"\n".join(body)+"\n\\end{document}\n"
    if tex.count(r"\begin{table}")!=counts["tables"] or tex.count(r"\begin{figure}")!=counts["figures"]:
        raise AssertionError("Generated structure count mismatch")
    if counts["headings"]!=sum(bool(HEADING.fullmatch(line.strip())) for line in lines):
        raise AssertionError("A manuscript heading was lost")
    return tex,{"source_sha256":source_hash,"exporter_sha256":exporter_hash,"counts":counts,"assets":assets}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source",type=Path,default=ROOT/"paper"/"paper.md")
    parser.add_argument("--output",type=Path,default=ROOT/"paper"/"paper.tex")
    parser.add_argument("--check-only",action="store_true",help="Validate conversion and assets without writing LaTeX")
    args=parser.parse_args()
    tex,record=convert(args.source.resolve(),args.output.resolve())
    if not args.check_only:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(tex,encoding="utf-8",newline="\n")
    print(json.dumps({"output":str(args.output),"written":not args.check_only,"compiled":False,**record},indent=2))


if __name__=="__main__":
    main()
