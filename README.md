# Python Poetry Managed Cookiecutter template

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=plastic)](https://github.com/alanwilter/poetry-python-cookiecutter/graphs/commit-activity)
[![GitHub](https://img.shields.io/github/license/alanwilter/poetry-python-cookiecutter?style=plastic)](https://github.com/alanwilter/poetry-python-cookiecutter)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/alanwilter/poetry-python-cookiecutter?display_name=tag&logo=github&style=plastic)](https://github.com/alanwilter/poetry-python-cookiecutter)
[![GitHub Release](https://img.shields.io/github/release-date/alanwilter/poetry-python-cookiecutter?style=plastic&logo=github)](https://github.com/alanwilter/poetry-python-cookiecutter)
[![Poetry](https://img.shields.io/endpoint?style=plastic&url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?style=plastic&url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=plastic)](https://github.com/pre-commit/pre-commit)

This is a [`cookiecutter`](https://cookiecutter.readthedocs.io) template that utilises [`poetry`](https://python-poetry.org/), [`ruff`](<https://github.com/joestubbs/ruff](https://github.com/astral-sh/ruff)>), [`pre-commit`](https://pre-commit.com/), and [`mypy`](http://mypy-lang.org/).

## How to Use

1. Install poetry, via `homebrew` or [`pipx`](https://github.com/pypa/pipx):

   ```bash
   brew install poetry
   # or
   pipx install poetry
   ```

2. Create a Python virtual environment of your preference and activate it.

3. Install `cookiecutter` and [`cruft`](https://github.com/cruft/cruft) via, e.g., [`homebrew`](https://brew.sh/) or `pip`:

   ```bash
   python3 -m pip install --upgrade cookiecutter cruft
   ```

4. Run the command below to create your new project based on this cookiecutter template:

   ```bash
   cookiecutter https://github.com/alanwilter/poetry-python-cookiecutter

   # or

   cookiecutter gh:/alanwilter/poetry-python-cookiecutter
   ```

   Alternatively, you can use `cruft`, which is a layer above `cookiecutter`. This allows you to manage your project from the template after it has been generated, enabling you to check, diff, or update it:

   ```bash
   cruft create https://github.com/alanwilter/poetry-python-cookiecutter
   ```

   The command line interface will ask you to provide several informations.

5. It's optional, but we strongly recommend [`commitizen`](https://github.com/commitizen-tools/commitizen)

## Not Exactly What You Want?

If this template doesn't meet your needs, you can explore thousands of other `cookiecutter` templates [here](https://github.com/search?q=cookiecutter&amp%3Btype=Repositories&type=repositories).
