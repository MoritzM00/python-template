# Light-weight Python Template

Tired of overloaded python templates? This template is for you!

This [demo repository](https://github.com/MoritzM00/python-template-demo) shows the template in action.

## Features

- [x] [Poetry](https://python-poetry.org/) for dependency management
- [x] [Pre-Commit](https://pre-commit.com/) for enforcing code quality
- [x] CI/CD with [Pre-Commit CI](https://pre-commit.ci/) and GitHub Actions
- [x] Light-weight Documentation with [pdoc](https://pdoc.dev/) with deployment to GitHub Pages

## Quick Start

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html), e.g. with

   ```bash
   pip install --user cookiecutter
   ```

2. Run the following command:

   ```bash
   cookiecutter https://github.com/MoritzM00/python-template
   ```

3. Follow the _Quick Start_ instructions in the README.md of your new project to setup the environment.
   Shortcut:

   ```bash
   make setup
   make activate
   ```

   Finally, commit the `poetry.lock` file to your repository.

4. Push your local repository to Github with the Github CLI:
   For this, run

   ```bash
   gh repo create
   ```

   to interactively create a new repository on Github.

5. Enable [Pre-Commit CI](https://pre-commit.ci/) for your repository.
6. Enable **Github Pages** for your documentation.
   To do that, go to the _Settings_ tab of your repository and scroll down to the _Pages_ section.
   For the _Source_ option, select _GitHub Action_.
