#!/usr/bin/env python3
"""Read-only, bounded interface-craft catalog search; standard library only."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True

DOMAINS = {
    "style": ("style", "styles.csv"),
    "palette": ("color", "colors.csv"),
    "fonts": ("typography", "typography.csv"),
    "layout": ("landing", "landing.csv"),
    "chart": ("chart", "charts.csv"),
}
FIELDS = {
    "style": ("Style ID", "Style Category", "Status", "Parent Style ID", "Preferred Mode",
              "Type", "Keywords", "Primary Colors", "Effects & Animation", "Best For",
              "Do Not Use For", "Performance", "Accessibility"),
    "palette": ("Product Type", "Primary", "On Primary", "Secondary", "On Secondary",
                "Accent", "On Accent", "Background", "Foreground", "Card", "Card Foreground",
                "Muted", "Muted Foreground", "Border", "Destructive", "On Destructive", "Ring", "Notes"),
    "fonts": ("Font Pairing Name", "Category", "Heading Font", "Body Font",
              "Mood/Style Keywords", "Best For", "Local Font Resources", "Notes"),
    "layout": ("Pattern ID", "Pattern Name", "Keywords", "Section Order",
               "Primary CTA Placement", "Conversion Optimization"),
    "chart": ("Data Type", "Best Chart Type", "Secondary Options", "When to Use",
              "When NOT to Use", "Color Guidance", "Accessibility Risk", "Accessibility Notes", "A11y Fallback"),
}


def bounded_limit(value):
    number = int(value)
    if not 1 <= number <= 5:
        raise argparse.ArgumentTypeError("limit must be from 1 to 5")
    return number


def run(domain, query, limit):
    root = Path(__file__).resolve().parent.parent
    source = json.loads((root / "references/catalog-provenance.json").read_text(encoding="utf-8"))
    core_domain, filename = DOMAINS[domain]
    for relative in ("scripts/catalog_core.py", f"data/{filename}"):
        record = source["files"][relative]
        digest = hashlib.sha256((root / relative).read_bytes()).hexdigest()
        if digest != record["sha256"]:
            raise ValueError(f"catalog integrity mismatch: {relative}")

    # The pinned core is imported only after verification. Its broader routing,
    # stack search and upstream generators are not exposed by this command.
    import catalog_core
    result = catalog_core.search(query, domain=core_domain, max_results=limit, diagnostics=True)
    if result.get("error"):
        raise ValueError(result["error"])
    with (root / "data" / filename).open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    identity = FIELDS[domain][0]
    indexed = {row[identity]: row for row in rows}
    candidates = []
    for item in result["results"]:
        row = indexed[item[identity]]
        candidates.append({field: row[field] for field in FIELDS[domain] if row.get(field)})
    output = {
        "domain": domain,
        "query": query,
        "count": len(candidates),
        "candidates": candidates,
        "diagnostics": result.get("diagnostics", {}),
        "source": {"repository": source["repository"], "commit": source["commit"],
                   "url": source["files"][f"data/{filename}"]["source_url"]},
        "guidance": "Candidates only; the brief, incumbent design and verified requirements take precedence. Source accessibility labels are not verification.",
    }
    for optional in ("redirect", "suggestions"):
        if optional in result:
            output[optional] = result[optional]
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("domain", choices=DOMAINS)
    parser.add_argument("query", help="English product/treatment terms or a named identity")
    parser.add_argument("--limit", type=bounded_limit, default=3)
    args = parser.parse_args()
    if not args.query.strip():
        parser.error("query cannot be empty")
    try:
        output = run(args.domain, args.query.strip(), args.limit)
    except (OSError, ValueError, KeyError, csv.Error, UnicodeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
