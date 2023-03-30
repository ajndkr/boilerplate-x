CLI_OPTIONS = ["y", "n"]
CLI_OPTIONS_FULL = {"y": "yes", "n": "no"}

DESCRIPTION = "You are an agent to create boilerplate code in any programming language for a given project idea."
PROJECT_STRUCTURE_TEMPLATE = template = """{description}

The git repository is empty and you need to create a list of files required for the project idea. Include all relevant files usually found in a git repository.

The list should be in YAML format. You MUST format the YAML as follows:
- foo
- bar/xzy.abc
- bar/xyz.def

Customisations:
Unit tests: {unit_tests}
Dockerization: {dockerization}
Github Actions: {github_actions}
Pre-commit hooks: {pre_commit_hooks}

You must be clear and concise. No explanations required. Make sure you do not include any irrelevant files or empty directories.

Project idea: {project_idea}
YAML Output:"""
PROJECT_FILE_TEMPLATE = """{description}

Project idea: {project_idea}

Project structure:
{project_structure}

You have to create file content based on the following project structure. The file content MUST be related to the project idea and structure.

ONLY create file content for the file name specified below. You must be clear and concise. No explanations required.

File name: {file_name}
File content:"""

DEFAULT_COMMIT_MESSAGE = "Initial commit (auto-commit by boilerplate-x)"
DEFAULT_REMOTE = "origin"
