# {{cookiecutter.project_name}}

![Tests](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/test_deploy.yaml?style={{cookiecutter.badge_style}}&label=Test%20and%20Deploy)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style={{cookiecutter.badge_style}})][pre-commit]
![License](https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}?style={{cookiecutter.badge_style}})

[pre-commit]: https://github.com/pre-commit/pre-commit

---

## Quick Start

Below you can find the quick start guide for development.

### Set up the environment

1. Set up the environment:

```bash
make setup
```

### Additional first-time setup

1. Enable [Pre-Commit CI](https://pre-commit.ci/) for your repository.
2. Enable **Github Pages** for your documentation.
   To do that, go to the _Settings_ tab of your repository and scroll down to the _GitHub Pages_ section.
   For the _Source_ option, select _GitHub Action_. Done!

### Documentation

The Documentation is automatically deployed to GitHub Pages.

To view the documentation locally, run:

```bash
make docs_view
```

## Credits

This project was generated with the [Light-weight Python Template](https://github.com/MoritzM00/python-template) by Moritz Mistol.
