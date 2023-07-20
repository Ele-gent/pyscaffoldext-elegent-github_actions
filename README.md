[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)
[![tests](https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions/actions/workflows/ci.yml/badge.svg)](https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions/actions/workflows/ci.yml)

# pyscaffoldext-elegent-github_actions

> a custom pyscaffold extension for github actions in Elegent style

To be used with PyScaffold if you want the custom Elegent ci files instead of the standard ones from PyScaffold.

## Installation

To install it, either clone this repo locally and install:

```bash
# cloning the repo via SSH
git clone git@github.com:Ele-gent/pyscaffoldext-elegent-github_actions.git
# or via GitHub CLI
gh repo clone Ele-gent/pyscaffoldext-elegent-github_actions
# move to the folder
cd pyscaffoldext-elegent-github_actions
# activate your desired environment, either via conda
source activate CONDA_ENV
# or a venv
source /path/to/venv/location/.venv/bin/activate
# install this package
python -m pip install elegentstyles
```

or download straight from github:

```bash
# activate your desired environment, either via conda
source activate CONDA_ENV
# or a venv
source /path/to/venv/location/.venv/bin/activate
# install this package
python -m pip install git+https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions.git
```

Specific version can be installed through specifying branches (only recommended for work in progress) or using one of the [tags](https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions/tags):
```bash
# some branch
python -m pip install git+https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions.git@hotfix-feature-xxx
# some version
python -m pip install git+https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions.git@v1.0.0
```

Note that `putup -h` shows a new option `--elegent-github-actions`.

## Usage

```shell
putup --elegent-github-actions
```

*NOTE*: can be used in combination with other options!

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.

created with

putup --custom-extension --markdown pyscaffoldext-elegent-github_actions
