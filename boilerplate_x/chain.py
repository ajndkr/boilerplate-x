from langchain import LLMChain, PromptTemplate
from langchain.schema import BaseLanguageModel

from .constants import (
    DESCRIPTION,
    GENERATE_PROJECT_STRUCTURE_TEMPLATE,
    PROJECT_FILE_TEMPLATE,
    UPDATE_PROJECT_STRUCTURE_TEMPLATE,
)


def load_generate_project_structure_chain(
    llm: BaseLanguageModel, verbose: bool = False
):
    """Loads the project structure chain."""
    prompt = PromptTemplate(
        template=GENERATE_PROJECT_STRUCTURE_TEMPLATE,
        input_variables=[
            "project_idea",
        ],
        partial_variables={"description": DESCRIPTION},
    )
    return LLMChain(prompt=prompt, llm=llm, verbose=verbose)


def load_update_project_structure_chain(llm: BaseLanguageModel, verbose: bool = False):
    """Loads the update project structure chain."""
    prompt = PromptTemplate(
        template=UPDATE_PROJECT_STRUCTURE_TEMPLATE,
        input_variables=[
            "project_idea",
            "project_structure",
            "unit_tests",
            "dockerization",
            "github_actions",
            "pre_commit_hooks",
        ],
        partial_variables={"description": DESCRIPTION},
    )
    return LLMChain(prompt=prompt, llm=llm, verbose=verbose)


def load_project_file_chain(llm: BaseLanguageModel, verbose: bool = False):
    """Loads the project file chain."""
    prompt = PromptTemplate(
        template=PROJECT_FILE_TEMPLATE,
        input_variables=["project_idea", "project_structure", "file_name"],
        partial_variables={
            "description": DESCRIPTION,
        },
    )
    return LLMChain(prompt=prompt, llm=llm, verbose=verbose)
