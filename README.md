# Light-weight Python Template

---

Tired of overloaded python templates? This template is for you!

This [demo repository](https://github.com/MoritzM00/python-template-demo) shows the template in action.

## Features

:white_check_mark: [Poetry](https://python-poetry.org/) for efficient dependency management

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
   cookiecutter https://github.com/MoritzM00/python-template
   ```

## Detailed Instructions for first-time setup

### Pre-Requisites

- Python >= 3.9
- [Poetry](https://python-poetry.org/docs/#installation)

The code is tested for python versions 3.9 and 3.10 on Linux and macOS.

### Environment Setup and GitHub Linking

After you generated your project with the template (see above), you need to do the following steps:

1. Setup your environment by executing

   ```bash
   make setup
   make activate
   ```

   and then create a commit (must include the `poetry.lock` file):

   ```bash
   git add .
   git commit -m "initial commit"
   ```

2. Push your local repository to Github with the Github CLI:
   For this, run

   ```bash
   gh repo create
   ```

   to interactively create a new repository on Github.

### Set up third-party services

1. Enable [Pre-Commit CI](https://pre-commit.ci/) for your repository.
2. Enable **Github Pages** for your documentation.
   To do that, go to the _Settings_ tab of your repository and scroll down to the _Pages_ section.
   For the _Source_ option, select _GitHub Action_.
