# SPARQL Queries

[SPARQL](https://www.w3.org/TR/rdf-sparql-query/) is a W3C standard query language for RDF. This directory contains useful SPARQL queries for validating and reporting on the Neurological Disease Ontology.

SPARQL queries are executed on the ontology files using [ROBOT](http://robot.obolibrary.org/), which allows easy execution over any OBO-format or OWL file. The queries run against both `nd-edit.owl` and downstream products.

## Query Types

### Constraint Violation Checks

These files are named `*violation.sparql`. A subset of these are configured in the Makefile and executed via the GitHub Actions CI/CD pipeline (`make test`). If any violation queries return results, the build will fail.

Common violations checked:
- `owldef-self-reference-violation.sparql` - Detects circular definitions
- `iri-range-violation.sparql` - Validates IRI ranges
- `label-with-iri-violation.sparql` - Checks for malformed labels
- `multiple-replaced_by-violation.sparql` - Ensures proper term deprecation
- `dc-properties-violation.sparql` - Validates Dublin Core properties

### Construct Queries

These files are named `construct*.sparql` and use the SPARQL `CONSTRUCT` clause. They generate new OWL axioms that can be inserted back into the ontology for automated enrichment.

### Report Queries

The remaining SPARQL queries are for informative purposes, generating useful reports about the ontology:
- `basic-report.sparql` - Overall ontology statistics
- `class-count-by-prefix.sparql` - Term counts by namespace
- `edges.sparql` - Relationship report
- `xrefs.sparql` - Cross-reference report
- `obsoletes.sparql` - Deprecated terms report
- `synonyms.sparql` - Synonym listing

## Running SPARQL Checks

SPARQL validation runs automatically as part of the build process:

```bash
cd ../ontology
make test
```

Or run validation on a specific file:

```bash
robot query --input nd-edit.owl --select ../sparql/owldef-self-reference-violation.sparql
```