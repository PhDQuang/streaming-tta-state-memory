"""Build consolidated literature/candidate artifacts from auditable independent scans."""
from pathlib import Path
import re

import _bootstrap
from historytta.utils import write_json

ROOT = _bootstrap.ROOT
SCANS = ROOT / "research/scans"

MATRIX = [
    ("T1", "Controlled history interventions", [7,9,8,8,9,9,9,8,8]),
    ("R2", "Composition-specific cross-modal brittleness", [7,8,9,8,9,9,8,8,8]),
    ("S1", "Selective-risk transfer under vocabulary expansion", [6,8,8,8,9,9,8,7,8]),
    ("T2", "Prior-shift identifiability under feature failure", [6,9,8,6,8,8,9,8,7]),
    ("T3", "Mixture versus conditional calibration after adaptation", [6,8,7,8,8,9,9,7,8]),
    ("R1", "Generator dependence in synthetic model selection", [5,8,8,7,8,8,8,7,6]),
    ("R3", "Concept-role reversal after VLM debiasing", [6,8,8,7,8,8,7,7,8]),
    ("S2", "Human-prompt model-ranking transfer", [5,8,8,7,8,8,7,6,8]),
    ("S3", "Semantic metrics under loss of specificity", [5,7,8,8,9,9,8,6,9]),
]
WEIGHTS = [.20,.16,.14,.10,.14,.10,.08,.06,.02]


def main():
    literature = ["# Literature review\n\nReview date: 2026-09-08. Bounded primary-source review, not an exhaustive systematic review. Three independent scans cover streaming adaptation, open-vocabulary dense perception, and VLM robustness/composition/synthetic data. Most emphasis is 2023–2026, with necessary foundations. Evidence depth and unknowns are explicit per record. All external numerical results are author reports, never our experiments.\n",
    "## Synthesis\n\nRecent work shifts from nominal accuracy toward temporal deployment, confidence reliability, language-dependent evaluation, and source/generator shortcuts. Large pretrained encoders make strong frozen baselines essential. Several intuitive ideas are already occupied: long-term collapse and selective resets; synonym/vocabulary sensitivity; hard-positive brittleness; and synthetic source shortcuts. The useful residual questions isolate mechanisms with paired interventions and independent evaluation rather than add modules.\n\nWe considered nine projects before selection. The top three are controlled adaptation-history effects (T1), compositional training × multimodal perturbation interactions (R2), and selective-risk transfer after vocabulary expansion (S1). See topic_candidates.md and novelty_analysis.md for decision logic.\n",
    "## Coverage and limits\n\nSources include CVPR/ICCV/ECCV, NeurIPS, ICLR, ICML, WACV, BMVC, IJCV/TPAMI-linked records, arXiv, and official repositories. A targeted broad search is not an audit of every AAAI/Pattern Recognition paper or complete Google/Semantic Scholar citation graph. Some records are abstract-depth and explicitly lack exact datasets or tables; those missing details are not invented. Core selected-project works receive additional full-text/code inspection. Dated query trails remain in research/scans/*.md.\n"]
    sections = []
    for name, marker in [("adaptation", "## Three research candidates"), ("segmentation", "## Three candidates (not a final topic selection)"), ("robustness", "## Candidate R1")]:
        text = (SCANS / f"{name}.md").read_text(encoding="utf-8")
        prefix, rest = text.split(marker, 1)
        literature.append(f"\n## Independent {name} evidence ledger\n\n" + prefix)
        sections.append(f"\n## {name.capitalize()} candidate profiles\n\n" + marker + rest)
    literature.append("\n## Primary-researcher independent checks\n\n" + (SCANS / "root_novelty.md").read_text(encoding="utf-8"))
    (ROOT / "research/literature_review.md").write_text("\n".join(literature), encoding="utf-8")
    rows = []
    for code, name, scores in MATRIX:
        rows.append({"id":code, "title":name, "scores":scores, "weighted_score":round(sum(w*s for w,s in zip(WEIGHTS,scores)), 3)})
    rows.sort(key=lambda r:r["weighted_score"], reverse=True)
    table = ["| ID | Candidate | Novelty | Importance | Hypothesis | Feasibility | Clarity | Reproducibility | Data | Paper | Compute efficiency | Weighted |",
             "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for row in rows:
        table.append("| " + " | ".join([row["id"],row["title"], *map(str,row["scores"]),f'{row["weighted_score"]:.2f}']) + " |")
    header = "# Candidate projects and decision matrix\n\nGenerated after independent literature reviews; nine complete candidate profiles follow. Scores are subjective research judgments, not measurements. The weights prioritize scientific merit: novelty .20, importance .16, hypothesis .14, feasibility .10, experimental clarity .14, reproducibility .10, dataset quality .08, paper potential .06, compute efficiency .02. Local hardware was excluded from topic scoring. Estimates in individual profiles are unprofiled broad ranges; the selected project's concrete pilot is costed separately.\n\n" + "\n".join(table) + "\n\n## Shortlist before final selection\n\nT1, R2, and S1 advance to the adversarial comparison in novelty_analysis.md. This matrix generates a shortlist; the evidence-based final choice is documented separately in proposal.md. Generic versions of several candidates were defeated by prior work and deliberately retained in their profiles.\n"
    (ROOT / "research/topic_candidates.md").write_text(header + "\n".join(sections), encoding="utf-8")
    write_json(ROOT / "research/decision_matrix.json", {"weights":WEIGHTS,"rows":rows})

    # Prefer independently verified scan records; avoid duplicate title/eprint records.
    entries, seen = [], set()
    for name in ("adaptation", "segmentation", "robustness", "root"):
        bib = (SCANS / f"{name}.bib").read_text(encoding="utf-8")
        for entry in re.split(r"(?=@\w+\s*\{)", bib):
            if not entry.lstrip().startswith("@"):
                continue
            title = re.search(r"title\s*=\s*\{(.+?)\}\s*,", entry, re.S | re.I)
            eprint = re.search(r"eprint\s*=\s*\{([^}]+)\}", entry, re.I)
            identity = re.sub(r"[^a-z0-9]", "", (title.group(1) if title else entry.split(",")[0]).lower())
            eid = re.sub(r"v\d+$", "", eprint.group(1)) if eprint else None
            if identity in seen or (eid and eid in seen):
                continue
            seen.add(identity)
            if eid:
                seen.add(eid)
            entries.append(entry.strip())
    (ROOT / "research/references.bib").write_text("% Verified bibliographic records; see literature_review.md for evidence depth.\n\n" + "\n\n".join(entries) + "\n", encoding="utf-8")
    print({"candidates":len(rows),"bibliography_entries":len(entries),"top3":[r["id"] for r in rows[:3]]})


if __name__ == "__main__":
    main()
