# Getting Started

## For End Users

### Accessing the Ontology

The easiest way to browse and search the ND ontology is through the [OLS Browser](http://www.ebi.ac.uk/ols/ontologies/nd).

### Downloading the Ontology

Download the latest version from [purl.obolibrary.org/obo/nd](http://purl.obolibrary.org/obo/nd) in your preferred format:
- nd.owl (OWL format)
- nd.obo (OBO format)
- nd.json (JSON format)

## For Developers

### Using the Ontology in Code

**Python:**
```python
import pronto

ontology = pronto.Ontology("http://purl.obolibrary.org/obo/nd.owl")
for term in ontology.terms():
    print(term.id, term.name)
```

**Java:**
```java
OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
OWLOntology ont = manager.loadOntologyFromOntologyDocument(
    new URL("http://purl.obolibrary.org/obo/nd.owl")
);
```

## For Editors

### Setting Up a Development Environment

1. **Install Protege**: Download from [protege.stanford.edu](https://protege.stanford.edu/)
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/addiehl/neurological-disease-ontology.git
   cd neurological-disease-ontology
   ```
3. **Request an ID Range**: Contact the maintainers to get an ID range for your edits
4. **Read the Editor Guide**: See [src/ontology/README-editors.md](https://github.com/addiehl/neurological-disease-ontology/blob/main/src/ontology/README-editors.md)

### Building the Ontology

Once you have the repository set up:

```bash
cd src/ontology
make all          # Generate all products
make test         # Run quality control checks
```

For more build options, see the Makefile targets: `make help`

### Contributing Changes

1. Create a feature branch: `git checkout -b my-feature`
2. Make your edits in Protege (src/ontology/nd-edit.owl)
3. Test your changes: `make test`
4. Commit and push: `git commit -m "Add new terms" && git push`
5. Open a pull request on GitHub

See [Contributing](contributing.md) for detailed guidelines.
