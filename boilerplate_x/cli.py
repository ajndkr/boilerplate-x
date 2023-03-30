import getpass
import logging
import os

import click
from rich.logging import RichHandler

from .constants import CLI_OPTIONS, CLI_OPTIONS_FULL
from .generator import ProjectGenerator

logging.basicConfig(level=logging.INFO, handlers=[RichHandler(rich_tracebacks=True)])
logger = logging.getLogger(__name__)


def run(
    prompt: str,
    output_path: str,
    verbose: bool,
    customisation_kwargs: dict,
    github_repo_creator_kwargs: dict,
):
    """Runs ProjectGenerator."""
    generator = ProjectGenerator(
        prompt=prompt,
        output_path=output_path,
        verbose=verbose,
        customisation_kwargs=customisation_kwargs,
        github_repo_creator_kwargs=github_repo_creator_kwargs,
    )

    logger.info("Generating project template...")
    generator.generate_template()

    logger.info("Your project is now ready to use!")


@click.command()
@click.option("-p", "--prompt", required=True, help="Your project idea.")
@click.option(
    "-o",
    "--output-path",
    "output_path",
    required=True,
    help="The output path for the generated project template.",
)
@click.option(
    "-g",
    "--create-github-repo",
    "enable_github",
    is_flag=True,
    help="Create a GitHub repository for the generated project template.",
)
@click.option(
    "-c",
    "--customise",
    "enable_customisation",
    is_flag=True,
    help="Enable customisation options for the project.",
)
@click.option("-v", "--verbose", is_flag=True, help="Run in verbose mode.")
def main(
    prompt: str,
    output_path: str,
    enable_customisation: bool,
    enable_github: bool,
    verbose: bool,
):
    """Boilerplate-X CLI.

    Generates a project boilerplate at the specified output path based on your project idea.
    """
    logger.info("Welcome to Boilerplate-X CLI!")

    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            prompt="Enter your OpenAI API key: "
        )

    customisation_kwargs = {}
    if enable_customisation:
        logger.info(
            "You are have enabled customisation options. Please select the options you would like to enable."
        )
        for opt in [
            "unit_tests",
            "dockerization",
            "github_actions",
            "pre_commit_hooks",
        ]:
            customisation_kwargs[opt] = CLI_OPTIONS_FULL[
                click.prompt(
                    f"Enable {opt}?",
                    type=click.Choice(CLI_OPTIONS),
                    default="n",
                    show_choices=True,
                )
            ]

    github_repo_creator_kwargs = {}
    if enable_github:
        logger.info(
            "You are about to create a GitHub repository for your project. Please provide your GitHub personal access token. "
            "Visit https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token for more information."
            "Recommended scopes: 'repo', 'workflow'"
        )
        token = getpass.getpass(prompt="Enter your Github personal access token: ")
        repo_name = click.prompt("Enter the name of the repository")
        private = (
            click.prompt(
                "Make the repository private?",
                type=click.Choice(CLI_OPTIONS),
                default="n",
                show_choices=True,
            ).lower()
            == "y"
        )
        github_repo_creator_kwargs = {
            "token": token,
            "repo_name": repo_name,
            "private": private,
            "target_folder": output_path,
        }

    run(prompt, output_path, verbose, customisation_kwargs, github_repo_creator_kwargs)


if __name__ == "__main__":
    main()
