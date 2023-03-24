class ProjectGenerator:
    """Generates a project template based on the project idea."""

    def __init__(self, prompt: str, output_path: str) -> None:
        """Constructor.

        Args:
            prompt: The project idea.
            output_path: The output path for the generated project template.
        """
        self.prompt = prompt
        self.output_path = output_path

    def generate_template(self) -> None:
        """Generates the project template."""
        self._generate_project_structure()
        self._generate_project_files()

    def _generate_project_structure(self) -> None:
        """Generates the project structure."""
        pass

    def _generate_project_files(self) -> None:
        """Generates the project files."""
        pass
