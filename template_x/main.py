import logging

import click

from .generator import ProjectGenerator

logger = logging.getLogger(__name__)


@click.command()
@click.option("--prompt", required=True, help="Your project idea.")
@click.option(
    "--output_path",
    required=True,
    help="The output path for the generated project template.",
)
def cli(prompt: str, output_path: str):
    """Template-X CLI.

    Generates a project template at the specified output path based on your project idea.
    """
    logger.info(f"Generating project template for '{prompt}' at '{output_path}'")

    generator = ProjectGenerator(prompt, output_path)
    generator.generate_template()

    logger.info("Project template ready!")


if __name__ == "__main__":
    cli()
