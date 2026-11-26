# Legacy files

These are the files from before the repository moved to the Ontology Development Kit. They are kept for reference only. Do not edit them.

- `ND.owl`: the last hand-maintained version of ND. Its content was migrated into [`../nd-edit.owl`](../nd-edit.owl) by [`../../scripts/migrate_legacy_nd.py`](../../scripts/migrate_legacy_nd.py), which documents exactly what changed.
- `*_import*.owl`: the old import modules. They are replaced by the ODK modules in [`../imports`](../imports), built with `sh run.sh make refresh-imports`.
- `MSPD_4.owl`: the MSPD ontology, which builds on ND. It has not been migrated yet.

All edits to ND go in `nd-edit.owl`; see [`../README-editors.md`](../README-editors.md).
