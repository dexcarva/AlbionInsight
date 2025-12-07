# Contributing to Albion Insight

**[Leia em Português (Brasil)](docs/pt-BR/contributing.md)** | **[Leia em Português (Portugal)](docs/pt-PT/contributing.md)**
**[Leer en Español](docs/es-ES/contributing.md)**
**[Lire en Français](docs/fr-FR/contributing.md)**
**[Read in Arabic (اقرأ بالعربية)](docs/ar-SA/contributing.md)**
**[Czytaj po Polsku](docs/pl-PL/contributing.md)**
**[Lesen Sie auf Deutsch](docs/de-DE/contributing.md)**
**[Read in Hindi (हिंदी में पढ़ें)](docs/hi-IN/contributing.md)**
**[Read in Thai (อ่านเป็นภาษาไทย)](docs/th-TH/contributing.md)**
**[Read in Korean (한국어로 읽기)](docs/ko-KR/contributing.md)**
**[Přečtěte si v Češtině](docs/cs-CZ/contributing.md)**
**[Læs på Dansk](docs/da-DK/contributing.md)**
**[Διαβάστε στα Ελληνικά](docs/el-GR/contributing.md)**
**[بخوانید به فارسی](docs/fa-IR/contributing.md)**
**[Lue Suomeksi](docs/fi-FI/contributing.md)**
**[Basahin sa Filipino](docs/fil-PH/contributing.md)**
**[קראו בעברית](docs/he-IL/contributing.md)**
**[Baca dalam Bahasa Melayu](docs/ms-MY/contributing.md)**
**[Монгол хэлээр унших](docs/mn-MN/contributing.md)**
**[Citiți în Română](docs/ro-RO/contributing.md)**
**[Читати Українською](docs/uk-UA/contributing.md)**

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
pip install -r requirements-dev.txt

# Set up pre-commit hooks (optional but recommended)
pre-commit install
```

### Running the Application

```bash
# On Linux/macOS:
sudo venv/bin/python3 -m albion_insight

# On Windows (as Administrator):
python -m albion_insight
```

## Coding Standards

We follow PEP 8 style guidelines for Python code. Please ensure your code adheres to these standards:

- Use 4 spaces for indentation (no tabs)
- Maximum line length of 100 characters
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Include type hints where appropriate
- Keep functions focused and concise

**Tools to help (run these before committing):**

```bash
# Format your code with black and isort
black albion_insight/
isort albion_insight/

# Check for style issues
flake8 albion_insight/

# Run type checking
mypy albion_insight/

# Run linter
pylint albion_insight/
```

**Automated Quality Checks:**

We use `pre-commit` hooks to automatically check code quality before commits. If you've installed pre-commit hooks, they will run automatically on `git commit`. To run them manually:

```bash
pre-commit run --all-files
```

## Commit Messages

We follow the **Conventional Commits** specification for clear and structured commit messages:

**Format:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat:` A new feature
- `fix:` A bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, missing semicolons, etc.)
- `refactor:` Code refactoring without feature changes
- `perf:` Performance improvements
- `test:` Adding or updating tests
- `chore:` Build process, dependencies, or tooling changes

**Examples:**
```
feat(damage-meter): Add export functionality for DPS reports

Implement CSV export feature for damage meter data,
allowing users to save combat statistics for analysis.

Closes #123

fix(network): Resolve IPv6 packet parsing issue

Update packet parser to correctly handle IPv6 addresses
in network traffic analysis.

docs(readme): Add macOS installation instructions

style(code): Format imports with isort

refactor(core): Reorganize network tracking module
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
