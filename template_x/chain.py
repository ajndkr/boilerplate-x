from langchain import LLMChain, PromptTemplate
from langchain.schema import BaseLanguageModel

TEMPLATE_X_DESCRIPTION = "You are template-x: A python package to create github project templates for any programming language in minutes, with just an idea."
PROJECT_STRUCTURE_TEMPLATE = template = """{template_x_description}

The git repository is empty and you need to create a list of files required for the project idea. Include all relevant files usually found in a git repository. Also include unit tests.

The list should be in YAML format. You MUST format the YAML as follows:
- foo
- bar/xzy.abc
- bar/xyz.def

You must be clear and concise. No explanations required.

Project idea: {project_idea}
YAML Output:"""
PROJECT_FILE_TEMPLATE = """{template_x_description}

Project idea: {project_idea}

Project structure:
{project_structure}

You have to create file content based on the following project structure. The file content MUST be related to the project idea and structure.

File name: {file_name}
File content:"""


def load_project_structure_chain(llm: BaseLanguageModel, verbose: bool = False):
    """Loads the project structure chain."""
    prompt = PromptTemplate(
        template=PROJECT_STRUCTURE_TEMPLATE,
        input_variables=["project_idea"],
        partial_variables={"template_x_description": TEMPLATE_X_DESCRIPTION},
    )
    return LLMChain(prompt=prompt, llm=llm, verbose=verbose)


def load_project_file_chain(llm: BaseLanguageModel, verbose: bool = False):
    """Loads the project file chain."""
    prompt = PromptTemplate(
        template=PROJECT_FILE_TEMPLATE,
        input_variables=["project_idea", "project_structure", "file_name"],
        partial_variables={
            "template_x_description": TEMPLATE_X_DESCRIPTION,
        },
    )
    return LLMChain(prompt=prompt, llm=llm, verbose=verbose)
