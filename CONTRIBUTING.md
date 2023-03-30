This document contains information about contributing to Boilerplate-X. Please read it before contributing.

## Setup Instructions

Boilerplate-X is built with Python 3.9 and managed by Poetry. Clone this repository and follow the steps below to get started.

### Create conda environment:

```bash
conda create -n boilerplate-x python=3.9
conda activate boilerplate-x
```

You can choose any other environment manager of your choice.

### Install dependencies:

```bash
pip install poetry
poetry install
```

## CI/CD

Boilerplate-X uses `pre-commit` to run code checks and tests before every commit. To install the pre-commit hooks, run the following commands:

```bash
pip install pre-commit
pre-commit install
```
