"""Test the `main` module."""
from {{cookiecutter.package_name}}.main import say_hello


def test_say_hello():
    """Test the `say_hello` function."""
    assert say_hello() == "Hello World!"
