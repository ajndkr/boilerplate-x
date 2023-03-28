import getpass
import logging
import os

import click

from .constants import _MAP
from .generator import ProjectGenerator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
    "--unit-tests",
    "unit_tests",
    is_flag=True,
    help="Generate unit tests for the project.",
)
@click.option(
    "--dockerization",
    "dockerization",
    is_flag=True,
    help="Generate Dockerfile for the project.",
)
@click.option(
    "--github-actions",
    "github_actions",
    is_flag=True,
    help="Generate GitHub Actions for the project.",
)
@click.option(
    "--pre-commit-hooks",
    "pre_commit_hooks",
    is_flag=True,
    help="Generate pre-commit hooks for the project.",
)
@click.option("-v", "--verbose", is_flag=True, help="Run in verbose mode.")
def main(
    prompt: str,
    output_path: str,
    verbose: bool,
    unit_tests: bool,
    dockerization: bool,
    github_actions: bool,
    pre_commit_hooks: bool,
):
    """Boilerplate-X CLI.

    Generates a project boilerplate at the specified output path based on your project idea.
    """
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            prompt="Enter your OpenAI API key: "
        )

    logger.info("Generating project...")

    customisation_kwargs = {
        "unit_tests": _MAP[unit_tests],
        "dockerization": _MAP[dockerization],
        "github_actions": _MAP[github_actions],
        "pre_commit_hooks": _MAP[pre_commit_hooks],
    }

    generator = ProjectGenerator(
        prompt=prompt,
        output_path=output_path,
        verbose=verbose,
        customisation_kwargs=customisation_kwargs,
    )
    generator.generate_template()

    logger.info(f"Your project is now available at {output_path}!")


if __name__ == "__main__":
    main()
