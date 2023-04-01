from pydantic import BaseModel, Field


class ChatOpenAISchema(BaseModel):
    temperature: float = 0.0
    request_timeout: int = 300


class ProjectStructureLLMSchema(ChatOpenAISchema):
    max_tokens: int = 256


class ProjectFileLLMSchema(ChatOpenAISchema):
    max_tokens: int = 2048


class ProjectGeneratorSchema(BaseModel):
    project_structure_llm: ProjectStructureLLMSchema = Field(
        default_factory=ProjectStructureLLMSchema
    )
    project_file_llm: ProjectFileLLMSchema = Field(default_factory=ProjectFileLLMSchema)
    project_structure_file_name: str = ".boilerplate_x"


class GithubRepoCreatorSchema(BaseModel):
    default_commit_message: str = "Initial commit"
    default_remote: str = "origin"
    user: str = "boilerplate-x"
    email: str = "boilerplate-x@noreply.github.com"
