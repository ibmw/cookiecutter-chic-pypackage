import pytest
from pytest_cookies.plugin import Cookies


def test_bake_with_defaults(cookies: Cookies) -> None:
    """Test bake the project with the default values."""
    result = cookies.bake()

    assert result.project_path.is_dir()
    assert result.project_path.name == "my-awesome-package-name"
    assert result.exit_code == 0
    assert result.exception is None

    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert "src" in found_toplevel_files
    assert "tests" in found_toplevel_files


def test_bake_with_custom_package_name(cookies: Cookies) -> None:
    """Test bake the project with a custom package name."""
    result = cookies.bake(extra_context={"package_name": "This is the Test"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert result.project_path.name == "this-is-the-test"


@pytest.mark.parametrize(
    ("context_key", "context_value", "file_paths", "is_activate"),
    [
        (
            "with_fastapi_api",
            "0",
            ["src/my_test_package/api.py", "tests/test_api.py"],
            False,
        ),
        (
            "with_streamlit_app",
            "0",
            ["src/my_test_package/app.py"],
            False,
        ),
        (
            "with_typer_cli",
            "0",
            ["src/my_test_package/cli.py", "tests/test_cli.py"],
            False,
        ),
        (
            "with_mkdocs",
            "0",
            ["docs/index.md", "mkdocs.yml"],
            False,
        ),
        (
            "with_code_of_conduct",
            "0",
            ["CODE_OF_CONDUCT.md"],
            False,
        ),
        (
            "with_contributing_file",
            "0",
            ["CONTRIBUTING.md"],
            False,
        ),
        (
            "with_security_file",
            "0",
            ["SECURITY.md"],
            False,
        ),
        (
            "development_environment",
            "simple",
            ["src/my_test_package/py.typed", ".github/dependabot.yml"],
            False,
        ),
        (
            "with_fastapi_api",
            "1",
            ["src/my_test_package/api.py", "tests/test_api.py"],
            True,
        ),
        ("with_streamlit_app", "1", ["src/my_test_package/app.py"], True),
        (
            "with_typer_cli",
            "1",
            ["src/my_test_package/cli.py", "tests/test_cli.py"],
            True,
        ),
        (
            "with_mkdocs",
            "1",
            ["docs/index.md", "mkdocs.yml"],
            True,
        ),
        ("with_code_of_conduct", "1", ["CODE_OF_CONDUCT.md"], True),
        ("with_contributing_file", "1", ["CONTRIBUTING.md"], True),
        ("with_security_file", "1", ["SECURITY.md"], True),
        (
            "development_environment",
            "strict",
            ["src/my_test_package/py.typed", ".github/dependabot.yml"],
            True,
        ),
    ],
)
def test_bake_with_options(
    cookies: Cookies,
    context_key: str,
    context_value: str,
    file_paths: list[str],
    is_activate: bool,
) -> None:
    """Test bake the project without "with" options and a custom package name."""
    result = cookies.bake(
        extra_context={
            "package_name": "My Test Package",
            context_key: context_value,
        },
    )

    assert result.project_path.name == "my-test-package"
    assert result.project_path.is_dir()
    assert result.exit_code == 0
    assert result.exception is None

    found_toplevel_files = [f.name for f in result.project_path.iterdir()]
    assert "src" in found_toplevel_files
    assert "tests" in found_toplevel_files

    package_name_kebab_name_path = result.project_path / "src/my_test_package"
    assert package_name_kebab_name_path.is_dir()
    assert package_name_kebab_name_path.name == "my_test_package"

    for file_path in file_paths:
        assert (result.project_path / file_path).is_file() == is_activate
