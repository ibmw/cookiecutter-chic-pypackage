from pathlib import Path

from cookiecutter.utils import rmtree

# Read Cookiecutter configuration.
package_name = "{{ cookiecutter.__package_name_snake_case }}"
development_environment = "{{ cookiecutter.development_environment }}"
with_fastapi_api = int("{{ cookiecutter.with_fastapi_api }}")
with_streamlit_app = int("{{ cookiecutter.with_streamlit_app }}")
with_typer_cli = int("{{ cookiecutter.with_typer_cli }}")
with_mkdocs = int("{{ cookiecutter.with_mkdocs }}")
with_code_of_conduct = int("{{ cookiecutter.with_code_of_conduct }}")
with_contributing_file = int("{{ cookiecutter.with_contributing_file }}")
with_security_file = int("{{ cookiecutter.with_security_file }}")
is_deployable_app = (
    "{{ not not cookiecutter.with_fastapi_api|int or not not cookiecutter.with_streamlit_app|int }}"  # noqa: PLR0133, E501
    == "True"
)
is_publishable_package = (
    "{{ not cookiecutter.with_fastapi_api|int and not cookiecutter.with_streamlit_app|int }}"  # noqa: PLR0133, E501
    == "True"
)


def remove_file(filepath: str) -> None:
    """
    Deletes the file located at the specified file path.

    This function attempts to delete a file using the provided file path. If the file
    does not exist or the program lacks the necessary permissions to delete the file,
    it will raise a FileNotFoundError or PermissionError respectively.

    Args:
        filepath (str): The path to the file to be deleted. This should be a valid
                        path string to a file.

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
        PermissionError: If the program lacks the necessary permissions to delete
            the file.
    """
    Path(filepath).unlink()


# Remove py.typed and Dependabot if not in strict mode.
if development_environment != "strict":
    remove_file(f"src/{package_name}/py.typed")
    remove_file(".github/dependabot.yml")

# Remove FastAPI if not selected.
if not with_fastapi_api:
    remove_file(f"src/{package_name}/api.py")
    remove_file("tests/test_api.py")

# Remove Streamlit if not selected.
if not with_streamlit_app:
    remove_file(f"src/{package_name}/app.py")

# Remove Typer if not selected.
if not with_typer_cli:
    remove_file(f"src/{package_name}/cli.py")
    remove_file("tests/test_cli.py")

# Remove mkdocs if not selected
if not with_mkdocs:
    rmtree("docs")
    remove_file("mkdocs.yml")

if not with_code_of_conduct:
    remove_file("CODE_OF_CONDUCT.md")

if not with_contributing_file:
    remove_file("CONTRIBUTING.md")

if not with_security_file:
    remove_file("SECURITY.md")

# Remove unused GitHub Actions workflows.
if not is_deployable_app:
    remove_file(".github/workflows/deploy.yml")
if not is_publishable_package:
    remove_file(".github/workflows/publish.yml")
