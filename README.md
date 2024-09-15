# Light-weight Python Template

---

Tired of overloaded python templates? This template is for you!

This [demo repository](https://github.com/MoritzM00/python-template-demo) shows the template in action.

## Features

:white_check_mark: [uv](https://docs.astral.sh/uv/) for efficient dependency management

**Note:** Need Conda as base environment for data Science and ML Projects? Switch to the `conda` Branch!

:white_check_mark: [Pre-Commit](https://pre-commit.com/) for enforcing code quality

:white_check_mark: CI/CD with [Pre-Commit CI](https://pre-commit.ci/) and GitHub Actions

:white_check_mark: Light-weight Documentation with [pdoc](https://pdoc.dev/) with deployment to GitHub Pages

## Quick Start

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/), e.g. with homebrew:

   ```bash
   brew install uv
   ```

2. Run the following command:

   ```bash
   uvx cookiecutter gh:MoritzM00/python-template
   ```

   or

   ```bash
   uvx cookiecutter -c conda gh:MoritzM00/python-template
   ```

   to get the conda template.

## Detailed Instructions for first-time setup

### Pre-Requisites

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

The code is tested for python versions 3.10 and 3.11 on Linux and version 3.10 on macOS.

### Environment Setup and GitHub Linking

After you generated your project with the template (see above), you need to do the following steps:

1. Setup your environment by executing

   ```bash
   make setup
   source .venv/bin/activate
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
