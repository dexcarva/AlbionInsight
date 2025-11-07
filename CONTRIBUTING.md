# Contributing to Albion Insight

**[Leia em Português do Brasil](CONTRIBUTING.pt-br.md)**

**[Leia em Português](CONTRIBUTING.pt-BR.md)**
**[Leer en Español](CONTRIBUTING.es-ES.md)**
**[Lire en Français](CONTRIBUTING.fr-FR.md)**

First off, thank you for considering contributing to Albion Insight! It's people like you that make Albion Insight such a great tool for the Albion Online community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Code Contributions](#code-contributions)
  - [Documentation](#documentation)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible using the bug report template.

**Good bug reports include:**
- A clear and descriptive title
- Exact steps to reproduce the problem
- Expected vs actual behavior
- Screenshots if applicable
- Your environment details (OS, Python version, etc.)
- Relevant logs or error messages

### Suggesting Features

Feature suggestions are welcome! Please use the feature request template and provide:
- A clear description of the feature
- The problem it solves
- Possible implementation approaches
- Any alternatives you've considered

### Code Contributions

We love code contributions! Here's how to get started:

1. **Fork the repository** and create your branch from `master`
2. **Set up your development environment** (see Development Setup below)
3. **Make your changes** following our coding standards
4. **Test your changes** thoroughly
5. **Update documentation** if needed
6. **Submit a pull request** using our PR template

### Documentation

Improvements to documentation are always appreciated! This includes:
- README files
- Wiki pages
- Code comments
- Tutorials and guides
- Translations to other languages

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Root/Administrator privileges (for packet capture)

### Setting Up Your Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pylint flake8 black pytest
```

### Running the Application

```bash
# On Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# On Windows (as Administrator):
python albion_insight.py
```

## Coding Standards

We follow PEP 8 style guidelines for Python code. Please ensure your code adheres to these standards:

- Use 4 spaces for indentation (no tabs)
- Maximum line length of 100 characters
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Include type hints where appropriate
- Keep functions focused and concise

**Tools to help:**
```bash
# Format your code with black
black albion_insight.py

# Check for style issues
flake8 albion_insight.py

# Run linter
pylint albion_insight.py
```

## Commit Messages

Write clear and meaningful commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests when relevant

**Examples:**
```
Add damage meter export functionality

Fix network packet parsing for IPv6 connections

Update README with macOS installation instructions

Closes #123
```

## Pull Request Process

1. **Update documentation** for any changes to functionality
2. **Add tests** for new features or bug fixes
3. **Ensure all tests pass** before submitting
4. **Update the README.md** if needed
5. **Fill out the PR template** completely
6. **Link related issues** in your PR description
7. **Request review** from maintainers
8. **Address feedback** promptly and professionally

### PR Checklist

Before submitting your PR, ensure:
- [ ] Code follows the project's style guidelines
- [ ] Self-review completed
- [ ] Comments added to complex code sections
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added and passing
- [ ] Dependent changes merged

## Questions?

Don't hesitate to ask questions! You can:
- Open an issue with the "question" label
- Join our community discussions
- Reach out to the maintainers

Thank you for contributing to Albion Insight! Your efforts help make this tool better for the entire Albion Online community.
