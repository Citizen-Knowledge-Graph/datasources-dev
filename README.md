# datendialog-dev

## Install
### Basic Requirements
#### Python Version
I recommend using _pyenv_ to install a fitting python version. To install pyenv, please follow allow (this documentation)[https://github.com/pyenv/pyenv?tab=readme-ov-file#installation]

After installing pyenv, please remember to set up the suggested (python build environment)[https://github.com/pyenv/pyenv/wiki#suggested-build-environment]

After installing pyenv, you can install a fitting python version:
```bash
pyenv install 3.12
```
#### Poetry
We use Python-Poetry for python virtual environment management. Please follow (this guide)[https://python-poetry.org/docs/#installation] to install Poetry.

### Setting Up Working Environment
Using pyenv, we can set the used python version in the working directory and install all required python packages.
```bash
pyenv local 3.12
poetry install
```
Poetry is set up for this repository to create a local virtual environment (see `poetry.toml`). Virtual Studio Code will automatically detect the local virtual environment and will use it for the jupyter notebook or python scripts.

Afterwards we can open a Poetry shell `poetry shell` or run the jupyter notebook in Visual Studio Code.

