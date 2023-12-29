import re

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
package_name = "{{ cookiecutter.package_name }}"

if not re.match(MODULE_REGEX, package_name):
    raise ValueError(f"ERROR: {package_name} is not a valid Python module name!")
