# Template-X - Create GitHub Project Templates in Minutes!

Template-X is a powerful and highly customizable Python package that enables you to create GitHub project templates for any programming language in just a few minutes. Have an idea? Turn it into a fully functional template with Template-X!

> DISCLAIMER! This project is highly experimental and is not ready for production use. Use at your own risk!

<img src="assets/logo.jpeg" alt="template-x-logo" width="200">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ajndkr/template-x/blob/main/LICENSE)

## 🚀 Features

- **Powered by chatGPT and Langchain**: Template-X uses OpenAI's chatGPT API and [Langchain](https://langchain.readthedocs.io/en/latest/) framework to generate your project template.
- **Create templates for any programming language**: Whether it's Python, JavaScript, Go, or any other language, Template-X has got you covered!
- **Easy to use**: Create a template with a single CLI command.
- **Fast**: Create templates in minutes, not hours.
- **Open source**: Template-X is open source and always will be. Contribute on [GitHub](https://github.com/ajndkr/template-x)!

Template-X has a collection of example templates to showcase its capabilities. You can find them in the `examples` folder.

## 📖 Table of Contents

- [Quickstart](#-quickstart)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)

## 💾 Installation

Template-X is built with Python 3.9 and maintained by Poetry.

```bash

git clone https://github.com/ajndkr/template-x.git
pip install poetry
poetry install
```

## 🎯 Quickstart

Creating a GitHub project template with Template-X is as simple as running the following CLI command:

```bash
template-x -p "your project idea" -o "path/to/project"
```

Now, you'll have a new folder at `path/to/project` containing your GitHub project template, which includes a `.gitignore`, `LICENSE`, `README.md`, and more!

## 🤝 Contributing

Contributions are more than welcome! If you have an idea for a new feature or want to help improve Template-X, please create an issue or submit a pull request
on [GitHub](https://github.com/ajndkr/template-x).

### CI/CD

- Install pre-commit

  ```bash
  pip install pre-commit
  pre-commit install
  ```

## ⚖️ License

Template-X is released under the [MIT License](https://github.com/ajndkr/template-x/blob/main/LICENSE).
