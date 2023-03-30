from langchain import LLMChain, PromptTemplate
from langchain.schema import BaseLanguageModel

from .constants import DESCRIPTION, PROJECT_FILE_TEMPLATE, PROJECT_STRUCTURE_TEMPLATE


def load_project_structure_chain(llm: BaseLanguageModel, verbose: bool = False):
    """Loads the project structure chain."""
    prompt = PromptTemplate(
        template=PROJECT_STRUCTURE_TEMPLATE,
        input_variables=["project_idea"],
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
