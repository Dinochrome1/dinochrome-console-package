from typer.testing import CliRunner

from dinochrome_console_package.main import app

runner = CliRunner()


def test_print_something():
    result = runner.invoke(app, ["print-something"])
    assert result.exit_code == 0
    assert result.stdout == "Alert! Portal gun shooting! 💥\n"


def test_main():
    result = runner.invoke(app)
    # result = runner.invoke(app, ["print-something"])
    assert result.exit_code == 0
    assert result.stdout == "Передай какие-нибудь подкоманды в командной строке! 💥\n"
