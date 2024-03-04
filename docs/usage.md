# 🚀 How to use ?

If you're looking for a straightforward way to create projects without needing to update them later with changes made to the original template, using Cookiecutter is recommended. In fact, you can always switch to cruft at a later date.

## Usage with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)

### Create a new Python project with this template:

1. Install cookiecutter using your prefered package manager

The recommended way to use Cookiecutter as a command line utility is to run it with [`pipx`](https://pypa.github.io/pipx/), which can be installed with `pip install pipx`, but if you plan to use Cookiecutter programmatically, please run `pip install cookiecutter` inside your virtual environement.

```sh
pipx install cookiecutter
``` 
2. Create a new repository for your Python project

The system will request that you input certain details. Following your inputs, it will generate a Python package within the existing directory, tailored to the information you've provided. To keep things concise, repositories on GitHub may simply adopt the 'gh' prefix

**Use a GitHub template**

```sh
pipx run cookiecutter gh:ibmw/cookiecutter-chic-pypackage
```

**Use a local template**

```bash
pipx run cookiecutter cookiecutter-chic-pypackage/
```

**Use it from Python**

```py
from cookiecutter.main import cookiecutter

# Create project from the cookiecutter-chic-pypackage/ template
cookiecutter('cookiecutter-chic-pypackage/')

# Create project from the ibmw/cookiecutter-chic-pypackage.git repo template
cookiecutter('gh:ibmw//cookiecutter-chic-pypackage.git')
```

### To use Cookiecutter programmatically

This repository is already configured with poetry, to install in full mode:

```sh
poetry install --with dev,test,docs --no-root
```
---
## Advanced usage with [Cruft](https://github.com/cruft/cruft)

Compare to Cookicutter, the main additionnal feature is the **Automatic Template Updates**, cruft automates the process of updating code to match the latest version of a template, making it easy to utilize template improvements across many projects.

This repository is already configured with Poetry.

### Creating a new Python project

To create a new Python project with this template:

1. Install cruft using your prefered python package manager

```sh
poetry install --no-root
``` 

2.  Create a new repository for your Python project

Upon providing required details, the system will generate a Python package in the current directory, customized with your inputs. Behind the scenes, cruft uses Cookiecutter to do the project expansion. The output will be identical except for the inclusion of a .cruft.json file, which holds the git hash of the template used and the variables you specified for the template.

```sh
poetry run cruft create -f https://github.com/ibmw/cookiecutter-chic-pypackage
```

### Updating your Python project

To update your Python project with the latest template:

1. Run `cruft update` to update your project with the latest template.
2. If any of the updates failed, resolve them by inspecting the generated `.rej` files.

### Linking an Existing Cookiecutter Project

If you previously created a project from this template directly with Cookiecutter, you can associate it with the original template by using:

```sh
poetry run cruft link -f https://github.com/ibmw/cookiecutter-chic-pypackage
```

Next, you have the option to designate the most recent commit of the template that the project has been synchronized with or choose to automatically align with the latest commit from the template as the default.