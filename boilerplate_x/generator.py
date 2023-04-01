import concurrent.futures
import logging
from pathlib import Path

import yaml
from langchain.chat_models import ChatOpenAI

from .chain import load_project_file_chain, load_project_structure_chain
from .github import GithubRepoCreator
from .schemas import ProjectGeneratorSchema

logger = logging.getLogger(__name__)
schema = ProjectGeneratorSchema()


class ProjectGenerator:
    """Generates a project boilerplate code based on the project idea."""

    def __init__(
        self,
        prompt: str,
        output_path: str,
        verbose: bool,
        customisation_kwargs: dict,
        github_repo_creator_kwargs: dict,
    ) -> None:
        """Constructor.

        Args:
            prompt: The project idea.
            output_path: The output path for the generated project template.
        """
        self.prompt = prompt
        self.output_path = output_path
        self.verbose = verbose
        self.customisation_kwargs = customisation_kwargs
        self.github_repo_creator_kwargs = github_repo_creator_kwargs

        self.project_structure_chain = load_project_structure_chain(
            ChatOpenAI(**schema.project_structure_llm.dict()), self.verbose
        )
        self.project_file_chain = load_project_file_chain(
            ChatOpenAI(**schema.project_file_llm.dict()), self.verbose
        )

        self.github_repo_url = None

    def generate_template(self) -> None:
        """Generates the project template."""
        project_structure = self._generate_project_structure()
        self._generate_project_files(project_structure)
        logger.info(f"Your project is now available at {self.output_path} !")

        if self.github_repo_creator_kwargs:
            logger.info("Pushing your project to GitHub...")
            github_repo_creator = GithubRepoCreator(**self.github_repo_creator_kwargs)
            self.github_repo_url = github_repo_creator.setup_github_repo()
            logger.info(
                f"Your GitHub repository is now available at {self.github_repo_url} !"
            )

    def _generate_project_structure(self) -> list[str]:
        """Generates the project structure."""
        project_structure_file = (
            Path(self.output_path) / schema.project_structure_file_name
        )
        if project_structure_file.exists():
            logger.info("Using cached project structure...")
            project_structure = yaml.safe_load(
                project_structure_file.read_text().strip()
            )
            return project_structure

        logger.info("Generating project structure...")
        chain_output = self.project_structure_chain.predict(
            project_idea=self.prompt, **self.customisation_kwargs
        )
        project_structure = yaml.safe_load(chain_output.strip())

        # cache the project structure
        self._write_file(
            schema.project_structure_file_name, yaml.safe_dump(project_structure)
        )

        return project_structure

    def _generate_project_files(self, project_structure: list[str]) -> None:
        """Generates the project files."""
        project_structure_str = yaml.safe_dump(project_structure)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for file_name in project_structure:
                if (Path(self.output_path) / file_name).exists():
                    logger.info(f"File already exists: {file_name}")
                    continue
                logger.info(f"Generating file content: {file_name}...")
                futures.append(
                    executor.submit(
                        self._generate_project_file, file_name, project_structure_str
                    )
                )
            for future in concurrent.futures.as_completed(futures):
                if future.exception() is not None:
                    logger.error(f"Failed to generate file: {future.exception()}")

    def _generate_project_file(
        self, file_name: str, project_structure_str: str
    ) -> None:
        """Generates a single project file."""
        file_content = self.project_file_chain.predict(
            project_idea=self.prompt,
            project_structure=project_structure_str,
            file_name=file_name,
        )
        self._write_file(file_name, file_content)

    def _write_file(self, file_name: str, file_content: str):
        """Writes the file to the output path."""
        file_path = Path(self.output_path) / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(file_content)
