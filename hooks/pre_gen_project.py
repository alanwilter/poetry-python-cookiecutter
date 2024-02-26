import os
import re
import sys
from shutil import which


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""
    return which(name) is not None


def check_valid_module_name():
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    module_name = "{{ cookiecutter.project_slug}}"

    if not re.match(MODULE_REGEX, module_name):
        print(
            f"""
        ERROR: The project slug ({module_name}) is not a valid Python module name.
        Please do not use a - and use _ instead
        """
        )

        # Exit to cancel project
        sys.exit(1)


def is_venv():
    venv = "VIRTUAL_ENV" in os.environ or "CONDA_PREFIX" in os.environ or "PIPENV_ACTIVE" in os.environ
    if not venv:
        print(
            """
        ERROR: This project requires a virtual environment.
        Please create one and activate it.
        """
        )
        sys.exit(3)


if __name__ == "__main__":
    is_venv()
    check_valid_module_name()
