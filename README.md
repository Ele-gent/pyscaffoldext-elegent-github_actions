[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)
[![tests](https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions/actions/workflows/ci.yml/badge.svg)](https://github.com/Ele-gent/pyscaffoldext-elegent-github_actions/actions/workflows/ci.yml)

# pyscaffoldext-elegent-github_actions

> a custom pyscaffold extension for github actions in Elegent style

To be used with PyScaffold if you want the custom Elegent ci files instead of the standard ones from PyScaffold.

## Installation

**NOTE**:
The recommandation is to have 1 conda environment to put all your pyscaffold-shenanigans in (pyscaffold, and all the elegent custom extensions).

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
# install this package in editable mode
python -m pip install -e pyscaffoldext-elegent-github_actions
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
putup TEST --elegent-github-actions
```

*NOTE*: can be used in combination with other options!

<!-- pyscaffold-notes -->

## Testing and developing workflows

Some changes to the github actions can be tested directly in the branch itself. However, I have found that for most of the changes, they need to be present in main before they can be triggered correctly. This means that against all normal recommendation, it seems that working on the main branch is needed here. When in doubt: try to add a dummy workflow file to a feature branch. Commit and push to origin. Now list the actions with  the GH CLI `gh workflow list`. Chances are slim that your new workflow will appear here.

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.

created with

putup --custom-extension --markdown pyscaffoldext-elegent-github_actions
