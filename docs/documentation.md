# Documentation

## Project Documentation

### Editor Guide
- **[README-editors.md](https://github.com/addiehl/neurological-disease-ontology/blob/main/src/ontology/README-editors.md)** - Complete guide for ontology editors covering ID ranges, imports, builds, and releases

### Quality Control
- **[SPARQL Documentation](https://github.com/addiehl/neurological-disease-ontology/blob/main/src/sparql/README.md)** - SPARQL query validation framework and reports

## External Resources

### Ontology Development
- [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit) - Our build and management framework
- [OBO Academy](https://oboacademy.github.io/obook/) - Comprehensive tutorials on ontology development
- [Gene Ontology Editors Tutorial](https://go-protege-tutorial.readthedocs.io/en/latest/) - Protege configuration and workflow

### Related Ontologies

The ND ontology integrates with these standard biomedical ontologies:

| Ontology | ID | Focus |
|----------|-------|-------|
| **BFO** | Basic Formal Ontology | Top-level upper ontology |
| **OBI** | Ontology for Biomedical Investigations | Research investigations and roles |
| **PR** | PRotein Ontology | Protein entities and modifications |
| **RO** | Relationship Ontology | Semantic relationships |
| **UBERON** | Uberon Anatomy | Anatomical structures |
| **OGMS** | Ontology of General Medical Science | Medical science concepts |

### Tools

- **[Protege](https://protege.stanford.edu/)** - Ontology editor
- **[ROBOT](http://robot.obolibrary.org/)** - Command-line ontology tool
- **[OLS](http://www.ebi.ac.uk/ols/)** - Ontology lookup service
- **[Ontobee](http://www.ontobee.org/)** - Term browser

## GitHub Pages

This documentation site is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and deployed automatically from the main branch.

To contribute to this documentation:
1. Edit files in the `docs/` directory
2. Create a pull request
3. Documentation will be automatically deployed upon merge

## Build Information

### Repository Structure

```
neurological-disease-ontology/
├── src/
│   ├── ontology/          # Main ontology files and Makefile
│   ├── metadata/          # PURL and OBO Foundry metadata
│   ├── sparql/            # SPARQL validation queries
│   └── scripts/           # Utility scripts
├── docs/                  # Documentation website (this site)
├── .github/workflows/     # GitHub Actions CI/CD
└── [release artifacts]    # Generated OWL, OBO, JSON files
```

### CI/CD Pipeline

The repository uses GitHub Actions for:
- **Quality Control** (qc.yml) - SPARQL validation, import checks
- **Documentation** (docs.yml) - Deployment to GitHub Pages

All checks run automatically on pull requests.

## License

The Neurological Disease Ontology is licensed under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/)
