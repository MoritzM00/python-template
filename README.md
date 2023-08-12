# Light-weight Python Template

---

Tired of overloaded python templates? This template is for you!

This [demo repository](https://github.com/MoritzM00/python-template-demo) shows the template in action.

## Features

:white_check_mark: [Poetry](https://python-poetry.org/) for efficient dependency management

:white_check_mark: [Conda](https://docs.conda.io/en/latest/) for data-science and machine learning projects

:white_check_mark: [Pre-Commit](https://pre-commit.com/) for enforcing code quality

:white_check_mark: CI/CD with [Pre-Commit CI](https://pre-commit.ci/) and GitHub Actions

:white_check_mark: Light-weight Documentation with [pdoc](https://pdoc.dev/) with deployment to GitHub Pages

## Quick Start

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html), e.g. with

   ```bash
   pip install cookiecutter
   ```

   or (preferably) with [Pipx](https://pypa.github.io/pipx/):

   ```bash
   pipx install cookiecutter
   ```

2. Run the following command:

   ```bash
   cookiecutter -c conda gh:MoritzM00/python-template
   ```

   or

   ```bash
   cookiecutter -c conda gh:MoritzM00/python-template
   ```

   to get the conda template.

## Detailed Instructions for first-time setup

### Pre-Requisites

- Python >= 3.9
- [Poetry](https://python-poetry.org/docs/#installation)

The code is tested for python versions 3.9 on Linux. Developed locally on MacOS.

### Setting up Git

First of all, initialize git,

```bash
git init
```

and commit the repo

```bash
git add .
git commit -m "Initial commit"
```

### Create the conda lock-files for the first time

If you do not have mamba, conda-lock and poetry installled, use the following bootstrap environment to create the lock files:

```bash
conda create -p /tmp/bootstrap -c conda-forge mamba conda-lock poetry='1.*'
conda activate /tmp/bootstrap
```

Then run

```bash
conda-lock -k explicit --conda mamba
```

and remove the bootstrap environment:

```bash
conda deactivate
rm -rf /tmp/bootstrap
```

Finally, commit the lock files to your repository.
From this point on, you can use the described workflow to create and update the lock files from above.

### Push to GitHub

For example with the `gh` CLI:

```bash
gh repo create
```

### Setting up GitHub Pages and Pre-Commit CI

1. Make sure that all lockfiles are up to date and committed.
2. Enable [Pre-Commit CI](https://pre-commit.ci/) for your repository.
3. Enable **Github Pages** for your documentation.
   To do that, go to the _Settings_ tab of your repository and scroll down to the _GitHub Pages_ section.
   For the _Source_ option, select _GitHub Action_. Done!
