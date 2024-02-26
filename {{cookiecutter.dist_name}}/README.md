# {{ cookiecutter.project_name }}

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=plastic)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}}/graphs/commit-activity)
[![GitHub](https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}}?style=plastic)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}})
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}}?display_name=tag&logo=github&style=plastic)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}})
[![GitHub Release](https://img.shields.io/github/release-date/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}}?style=plastic&logo=github)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}})
[![Poetry](https://img.shields.io/endpoint?style=plastic&url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?style=plastic&url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=plastic)](https://github.com/pre-commit/pre-commit)

## About The Project

{{cookiecutter.project_description}}

## Getting Started

To run this project locally, you will need to install the prerequisites and follow the installation section.

### Prerequisites

This Project depends on the [`poetry`](https://python-poetry.org/).

1. Install poetry, via `homebrew` or `pipx`:

   ```bash
   brew install poetry
   ```

   or

   ```bash
   pipx install poetry
   ```

2. Don't forget to use the python environment you set before and, if using `VScode`, apply it there.

3. It's optional, but we strongly recommend [`commitizen`](https://github.com/commitizen-tools/commitizen)

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.dist_name}}
   cd {{cookiecutter.dist_name}}
   ```
