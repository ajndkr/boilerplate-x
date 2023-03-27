import getpass
import logging
import os

import click

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
@click.option("-v", "--verbose", is_flag=True, help="Run in verbose mode.")
def main(prompt: str, output_path: str, verbose: bool):
    """Boilerplate-X CLI.

    Generates a project template at the specified output path based on your project idea.
    """
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass(
            prompt="Enter your OpenAI API key: "
        )

    logger.info(f"Generating project template for '{prompt}' at '{output_path}'")

    generator = ProjectGenerator(
        prompt=prompt, output_path=output_path, verbose=verbose
    )
    generator.generate_template()

    logger.info(f"Your project template is now available at {output_path}!")


if __name__ == "__main__":
    main()
