---
layout: ontology_detail
id: nd
title: Neurological Disease Ontology
jobs:
  - id: https://github.com/addiehl/neurological-disease-ontology/actions
    type: github-actions
build:
  checkout: git clone https://github.com/addiehl/neurological-disease-ontology.git
  system: git
  path: "."
contact:
  email: 
  label: 
  github: addiehl
description: Neurological Disease Ontology is an ontology for representing neurological diseases and related biomedical entities. It integrates entities from multiple foundational ontologies including Basic Formal Ontology, the Relationship Ontology, and anatomical entities from Uberon.
domains: [medicine, neurology]
homepage: https://github.com/addiehl/neurological-disease-ontology
products:
  - id: nd.owl
    name: "Neurological Disease Ontology OWL format"
  - id: nd.obo
    name: "Neurological Disease Ontology OBO format"
  - id: nd.json
    name: "Neurological Disease Ontology JSON format"
  - id: nd-base.owl
    name: "Neurological Disease Ontology base release (OWL)"
  - id: nd-base.obo
    name: "Neurological Disease Ontology base release (OBO)"
  - id: nd-base.json
    name: "Neurological Disease Ontology base release (JSON)"
  - id: nd-full.owl
    name: "Neurological Disease Ontology full release with imports (OWL)"
  - id: nd-full.obo
    name: "Neurological Disease Ontology full release with imports (OBO)"
  - id: nd-full.json
    name: "Neurological Disease Ontology full release with imports (JSON)"
  - id: nd-simple.owl
    name: "Neurological Disease Ontology simple release (OWL)"
  - id: nd-simple.obo
    name: "Neurological Disease Ontology simple release (OBO)"
  - id: nd-simple.json
    name: "Neurological Disease Ontology simple release (JSON)"
dependencies:
- id: bfo
- id: obi
- id: pr
- id: ro
- id: uberon
- id: ogms

tracker: https://github.com/addiehl/neurological-disease-ontology/issues
license:
  url: http://creativecommons.org/licenses/by/3.0/
  label: CC-BY
activity_status: active
---

The Neurological Disease Ontology (ND) is a comprehensive ontology representing neurological diseases and related biomedical entities. The ontology integrates entities from multiple foundational ontologies including the Basic Formal Ontology (BFO) for top-level entities, the Relationship Ontology (RO) for semantic relationships, anatomical structures from UBERON, and other specialized ontologies.

The ontology is developed using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit), which provides standardized tools and workflows for ontology development.

## Features

- Multiple release formats (OWL, OBO, JSON)
- Three release variants (full, base, simple)
- Integrated with foundational biomedical ontologies
- Automated quality control and validation
- Active development and maintenance

## Get Involved

- Browse the ontology: [OLS](http://www.ebi.ac.uk/ols/ontologies/nd)
- Report issues or request terms: [GitHub Issues](https://github.com/addiehl/neurological-disease-ontology/issues)
- Contributing guide: [CONTRIBUTING.md](https://github.com/addiehl/neurological-disease-ontology/blob/master/CONTRIBUTING.md)

