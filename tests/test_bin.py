from click.testing import CliRunner
from gcplogs.bin import cli


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
