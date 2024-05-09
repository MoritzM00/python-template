initialize_git:
	git init

venv:
	test -d venv || python -m venv venv

install: venv
	. venv/bin/activate && pip install -e ".[dev]"

setup: initialize_git install

test:
	pytest

docs_view:
	pdoc {{cookiecutter.package_name}} --docformat numpy

docs_save:
	pdoc {{cookiecutter.package_name}} -o docs --docformat numpy

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf venv
	rm -rf .pytest_cache
