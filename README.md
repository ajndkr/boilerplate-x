# Boilerplate-X - Create GitHub Project Boilerplate in Minutes!

Boilerplate-X is a chatGPT-powered solution to create GitHub project boilerplate for any programming language in just a few minutes. Have an idea? Turn it into a fully functional repository with Boilerplate-X!

> DISCLAIMER! This project is highly experimental and is not ready for production use. Use at your own risk!

## Why do I need this?

Starting a new project can be challenging, especially when it comes to writing basic, repetitive code. While there are many cookiecutter packages that help create an outline for your code, they aren't always tailored to your specific needs. Boilerplate-X, however, utilizes chatGPT to generate not only the foundational code like a cookiecutter but also actual code. This allows you to focus on developing unique features instead of spending hours setting up your repository.

<img src="https://raw.githubusercontent.com/ajndkr/boilerplate-x/main/assets/logo.jpeg" alt="boilerplate-x-logo" width="200">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ajndkr/boilerplate-x/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/boilerplate-x.svg)](https://pypi.org/project/boilerplate-x/)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/ajndkr/boilerplate-x)

## 🚀 Features

- **Powered by chatGPT and Langchain**: Boilerplate-X uses OpenAI's chatGPT API and [Langchain](https://langchain.readthedocs.io/en/latest/) framework to generate your project template.
- **Create boilerplate for any programming language**: Whether it's Python, JavaScript, Go, or any other language, Boilerplate-X has got you covered!
- **Easy to use**: Create a template with a single CLI command.
- **Fast**: Create boilerplate in minutes, not hours.
- **Customizable**: Boilerplate-X allows you to customize your template with available options, such as adding unit tests, CI/CD, and more.
- **Open source**: Boilerplate-X is open source and always will be. Contribute on [GitHub](https://github.com/ajndkr/boilerplate-x)!
- **GitHub integration**: Boilerplate-X integrates with GitHub to create a new repository for your project.

Boilerplate-X has a collection of example boilerplates. You can find them in the [`examples`](./examples/README.md) folder.

## 📖 Table of Contents

- [Quickstart](#-quickstart)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)

## 💾 Installation

Boilerplate-X is available on PyPI and can be installed via `pip`.

```bash
pip install boilerplate-x
```

## 🎯 Quickstart

Creating a GitHub project boilerplate with Boilerplate-X is as simple as running the following CLI command:

```bash
boilerplate-x -p "your project idea" -o "path/to/project"
```

Now, you'll have a new folder at `path/to/project` containing your GitHub project template, which includes a `.gitignore`, `LICENSE`, `README.md`, and more!

For more CLI options, run `boilerplate-x --help`.

## 🤝 Contributing

[![Code check](https://github.com/ajndkr/boilerplate-x/actions/workflows/code-check.yaml/badge.svg)](https://github.com/ajndkr/boilerplate-x/actions/workflows/code-check.yaml)
[![Publish](https://github.com/ajndkr/boilerplate-x/actions/workflows/publish.yaml/badge.svg)](https://github.com/ajndkr/boilerplate-x/actions/workflows/publish.yaml)

Contributions are more than welcome! If you have an idea for a new feature or want to help improve Boilerplate-X, please create an issue or submit a pull request
on [GitHub](https://github.com/ajndkr/boilerplate-x).

See [CONTRIBUTING.md](./CONTRIBUTING.md) for more information.

## ⚖️ License

Boilerplate-X is released under the [MIT License](https://github.com/ajndkr/boilerplate-x/blob/main/LICENSE).
