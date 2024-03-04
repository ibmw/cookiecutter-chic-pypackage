# Cookiecutter Chic PyPackage

A chic [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for scaffolding Python packages and apps. "Chic" denotes stylishness and sophistication, suitable for a sleek cookiecutter template to generate Python packages backbone.

Check [My Awesome Package Name](https://github.com/ibmw/my-awesome-package-name) for an example of a Python package and app that has been generated with this template.


## 💡 Out-of-the box Features

- 📦 Packaging and dependency management with [Poetry](https://github.com/python-poetry/poetry)
- ⚡ Task running with [Poe the Poet](https://github.com/nat-n/poethepoet)
- ✨ Code formatting with [Ruff](https://github.com/charliermarsh/ruff)
- 🧹 Code linting with [Pre-commit](https://pre-commit.com/), [Mypy](https://github.com/python/mypy), and [Ruff](https://github.com/charliermarsh/ruff)
- 🏷 Optionally follows the [Conventional Commits](https://www.conventionalcommits.org/) standard to automate [Semantic Versioning](https://semver.org/) and [Keep A Changelog](https://keepachangelog.com/) with [Commitizen](https://github.com/commitizen-tools/commitizen)
- ✅ Verified commits with [GPG](https://gnupg.org/)
- 🔄 Continuous integration with [GitHub Actions](https://docs.github.com/en/actions)
- 🧪 Testing with pytest and Test coverage with [Coverage.py](https://github.com/nedbat/coveragepy)
- 🏗 Scaffolding updates with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [Cruft](https://github.com/cruft/cruft)
- 🧰 Dependency updates with [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates)
- ⌨️ Command-line interface with [Typer](https://github.com/tiangolo/typer)
- 📖 Writting documentation in markdown style with [Mkdocs](https://github.com/mkdocs/mkdocs), Auto API doc generation and docstring template with [Mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
- 🌐 Host the documentation from [GitHub Pages](https://pages.github.com) with zero-config

## 🚀 Quickstart

### Simple usage with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)

To create a new Python project with this template:

1. Install cookiecutter using your prefered package manager

The recommended way to use Cookiecutter as a command line utility is to run it with [`pipx`](https://pypa.github.io/pipx/), which can be installed with `pip install pipx`, but if you plan to use Cookiecutter programmatically, please run `pip install cookiecutter` inside your virtual environement.

```sh
pipx install cookiecutter
``` 
2. Create a new repository for your Python project

The system will request that you input certain details. Following your inputs, it will generate a Python package within the existing directory, tailored to the information you've provided. To keep things concise, repositories on GitHub may simply adopt the 'gh' prefix

```sh
pipx run cookiecutter gh:ibmw/cookiecutter-chic-pypackage
```

### Advanced usage with [Cruft](https://github.com/cruft/cruft)

Compare to Cookicutter, the main additionnal feature is the **Automatic Template Updates**, cruft automates the process of updating code to match the latest version of a template, making it easy to utilize template improvements across many projects.

To create a new Python project with this template:

1. Install cruft using your prefered python package manager

```sh
pip install cruft
``` 

2.  Create a new repository for your Python project

Upon providing required details, the system will generate a Python package in the current directory, customized with your inputs. Behind the scenes, cruft uses Cookiecutter to do the project expansion. The output will be identical except for the inclusion of a .cruft.json file, which holds the git hash of the template used and the variables you specified for the template.

```sh
cruft create -f https://github.com/ibmw/cookiecutter-chic-pypackage
```

## 🌟 Credits

- Cookiecutter template for a modern Python packag: [fedejaure/cookiecutter-modern-pypackage](https://github.com/fedejaure/cookiecutter-modern-pypackage)
- 🐍 A modern Cookiecutter template for scaffolding Python packages and apps: [radix-ai/poetry-cookiecutter](https://github.com/radix-ai/poetry-cookiecutter)
- Hypermodern Python Cookiecutter: [cjolowicz/cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)