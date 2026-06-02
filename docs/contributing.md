# Contributing Guide

Thank you for your interest in contributing to the Neurological Disease Ontology!

## Code of Conduct

Please review our [Code of Conduct](https://github.com/addiehl/neurological-disease-ontology/blob/main/CODE_OF_CONDUCT.md) before participating.

## How to Contribute

### Reporting Issues

Found a problem with the ontology? Please [open an issue](https://github.com/addiehl/neurological-disease-ontology/issues/new) and include:
- Clear description of the problem
- Steps to reproduce (if applicable)
- Expected vs actual behavior
- Relevant terms or references

### Requesting New Terms

To suggest a new term:

1. **Check existing terms**: Search the ontology in [OLS](http://www.ebi.ac.uk/ols/ontologies/nd) first
2. **Open an issue**: Use the [term request template](https://github.com/addiehl/neurological-disease-ontology/issues/new/choose)
3. **Provide details**:
   - Term label and definition
   - Synonyms (if known)
   - Parent term in the hierarchy
   - References or literature support
   - ORCID (for attribution)

### Adding Terms Yourself

If you'd like to add terms directly:

1. **Get an ID range**: Contact maintainers to receive a unique ID range
2. **Set up your environment**: See [Getting Started - For Editors](getting-started.md#for-editors)
3. **Edit the ontology**: Open `src/ontology/nd-edit.owl` in Protege
4. **Test your changes**: Run `make test` in `src/ontology/`
5. **Create a pull request**: Follow the [pull request process](#pull-request-process)

## Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b issue-123-add-feature
   ```

2. **Make your changes**:
   - Edit `src/ontology/nd-edit.owl` in Protege
   - Keep commits focused and descriptive
   - Reference issue numbers in commit messages

3. **Run quality checks**:
   ```bash
   cd src/ontology
   make test
   ```

4. **Push and open a PR**:
   ```bash
   git push origin issue-123-add-feature
   ```
   Then create a pull request with a clear description

5. **Address review feedback**:
   - Respond to comments and suggestions
   - Push additional commits to resolve issues
   - Maintainers will merge when ready

## Development Workflow

### Building the Ontology

```bash
cd src/ontology

# Generate all products (OWL, OBO, JSON)
make all

# Run quality control checks
make test

# View all available commands
make help
```

### Validation Checks

The following checks run automatically:
- **SPARQL validation**: Structural and semantic consistency
- **Import validation**: External ontology consistency
- **ID range validation**: Ensures unique identifiers
- **GitHub Actions CI**: Automated testing on pull requests

## Standards and Best Practices

### Ontology Terms

- Use clear, descriptive labels
- Provide definitions with scientific references when possible
- Include appropriate synonyms
- Use proper relationship types (part_of, derives_from, etc.)

### Documentation

- Update relevant README files if your changes affect workflows
- Document new processes or configurations
- Use clear, accessible language

### Commits

- One logical change per commit
- Use descriptive commit messages
- Reference issue numbers: "Closes #123"
- Example: `Add terms for neurodegenerative diseases. Closes #42`

## Getting Help

- **Questions?**: Open a discussion in the [issue tracker](https://github.com/addiehl/neurological-disease-ontology/issues)
- **Documentation**: See [src/ontology/README-editors.md](https://github.com/addiehl/neurological-disease-ontology/blob/main/src/ontology/README-editors.md)
- **Training**: Check out [OBO Academy](https://oboacademy.github.io/obook/)

## Contact

For questions or to discuss contributions, please:
- Open an issue on GitHub
- Check the [main README](https://github.com/addiehl/neurological-disease-ontology) for maintainer contact info
