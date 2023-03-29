_MAP = {
    True: "yes",
    False: "no",
}

_DESCRIPTION = "You are an agent to create boilerplate code in any programming language for a given project idea."
_PROJECT_STRUCTURE_TEMPLATE = template = """{description}

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

You must be clear and concise. No explanations required.

Project idea: {project_idea}
YAML Output:"""
_PROJECT_FILE_TEMPLATE = """{description}

Project idea: {project_idea}

Project structure:
{project_structure}

You have to create file content based on the following project structure. The file content MUST be related to the project idea and structure. ONLY create file content for the file name specified below.

File name: {file_name}
File content:"""
