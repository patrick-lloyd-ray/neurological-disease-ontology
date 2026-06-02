
![Build Status](https://github.com/addiehl/neurological-disease-ontology/workflows/CI/badge.svg)
# Neurological Disease Ontology

A comprehensive ontology representing neurological diseases and related biomedical entities.

More information can be found at http://obofoundry.org/ontology/nd

## Overview

The Neurological Disease Ontology (ND) is developed using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit), which provides a standardized framework for ontology development including automated build processes, quality control, and release management.

## Versions

### Release versions

The latest version of the ontology is available in multiple formats:

- **OWL format**: http://purl.obolibrary.org/obo/nd.owl
- **OBO format**: http://purl.obolibrary.org/obo/nd.obo  
- **JSON format**: http://purl.obolibrary.org/obo/nd.json

The ontology is released in three variants:
- **nd-full**: Complete ontology with all imported terms
- **nd-base**: Base ontology without import closure
- **nd-simple**: Simplified version without complex axioms

(Note: The OBO Foundry registration is pending approval)

### Development version

Editors working on the ontology should use the development version:
- **[src/ontology/nd-edit.owl](src/ontology/nd-edit.owl)** - The master editing file

## Getting Started

### For End Users

Search for terms using [OLS](http://www.ebi.ac.uk/ols/ontologies/nd) or download the ontology files from the links above.

### For Editors

To contribute to the ontology:

1. **Read the contributor guidelines**: [CONTRIBUTING.md](CONTRIBUTING.md)
2. **Review editor documentation**: [src/ontology/README-editors.md](src/ontology/README-editors.md)
3. **Set up your environment**: 
   - Install [Protege](https://protege.stanford.edu/)
   - Clone this repository
   - Contact the maintainers for an ID range

## Building the Ontology

The ODK provides a standardized build process. To build locally:

```bash
cd src/ontology
make all
```

This generates all release artifacts in the standard formats. For more build targets, see the [editor documentation](src/ontology/README-editors.md).

## Quality Control

All changes are validated through:
- **SPARQL constraint checks** - Structural and semantic validation
- **Import validation** - Consistency of external ontology imports  
- **GitHub Actions CI/CD** - Automated testing on every commit

See [src/sparql/README.md](src/sparql/README.md) for details on SPARQL validation queries.

## Contact

Please use this GitHub repository's [Issue tracker](https://github.com/addiehl/neurological-disease-ontology/issues) to:
- Request new terms or features
- Report errors or concerns
- Discuss ontology development

## Acknowledgements

This ontology repository was created using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).