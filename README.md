# template-x

Create project templates for any programming language in minutes, with just an idea.

## Overview

- [Getting Started](#getting-started)
- [License](#license)

## Getting Started

### Setup

- Create conda environment

  ```bash
  conda create -n template-x python=3.9
  conda activate template-x
  ```

- Install poetry

  ```bash
  pip install poetry
  ```

- Install dependencies (via poetry)

  ```bash
  poetry install
  ```

### Usage

- Create a new project

  ```bash
  template-x -p <project-idea> -o <path-to-project>
  ```

### CI/CD

- Install pre-commit

  ```bash
  pip install pre-commit
  pre-commit install
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
