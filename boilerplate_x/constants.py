CLI_OPTIONS = ["y", "n"]
CLI_OPTIONS_FULL = {"y": "yes", "n": "no"}

DESCRIPTION = "You are an agent to create boilerplate code in any programming language for a given project idea."

GENERATE_PROJECT_STRUCTURE_TEMPLATE = template = """{description}

The git repository is empty and you need to create a list of files required for the project idea. Include all relevant files usually found in a git repository.

The list should be a `tree -ifF` output. Prefix each line with '-' character. Only include file names. You must be clear and concise. No explanations required. Make sure you do not include any irrelevant files or empty directories.

Project idea: {project_idea}

Output:"""

UPDATE_PROJECT_STRUCTURE_TEMPLATE = """{description}

Project idea: {project_idea}

Project structure:
{project_structure}

You have to update the project structure based on the following instructions:

Add Unit tests: {unit_tests}
Add Docker support: {dockerization}
Add Github Actions: {github_actions}
Add Pre-commit hooks: {pre_commit_hooks}

The list should be a `tree -ifF` output. Prefix each line with '-' character. You must be clear and concise. No explanations required.

Project structure:"""

PROJECT_FILE_TEMPLATE = """{description}

Project idea: {project_idea}

Project structure:
{project_structure}

You have to create file content based on the following project structure. The file content MUST be related to the project idea and structure.

ONLY create file content for the file name specified below. You must be clear and concise. No explanations required.

File name: {file_name}
File content:"""
