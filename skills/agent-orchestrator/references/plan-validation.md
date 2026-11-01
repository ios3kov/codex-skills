# Validate a declared file plan

For a file-only plan, the optional standard-library helper checks IDs, dependency cycles, path validity and unordered read/write conflicts:

```sh
python3 <skill-directory>/scripts/validate_plan.py /absolute/plan.json
```

The input is `{"tasks":[{"id":"inspect","depends_on":[],"reads":["src"],"writes":[],"acceptance":"Return source-linked findings"}]}`. Paths are workspace-relative; a directory owns its descendants. The checker reads this plan only. It does not inspect the filesystem, schedule or execute agents, validate symlinks, resolve case-insensitive aliases, or establish that a declared plan covers all shared resources. Review actual paths and non-file side effects separately. Exit 0 means the declared plan is structurally valid; exit 2 reports errors.
