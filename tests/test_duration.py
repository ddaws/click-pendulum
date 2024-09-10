import click
import pendulum
import pytest
from click.testing import CliRunner

from click_pendulum import Duration

CLICK_SUCCESS = 0


@click.command()
@click.option("--duration", type=Duration())
def cli(duration: pendulum.Duration):
    assert isinstance(duration, pendulum.Duration)
    click.echo(f"Duration: {duration}")


def test_valid_duration_short():
    runner = CliRunner()
    result = runner.invoke(cli, ["--duration", "3d 2m"])
    assert result.exit_code == CLICK_SUCCESS
    assert "Duration: 3 days 2 minutes" in result.output


def test_valid_duration_long():
    runner = CliRunner()
    result = runner.invoke(cli, ["--duration", "3 days 2 hours 4 minutes"])
    assert result.exit_code == CLICK_SUCCESS
    assert "Duration: 3 days 2 hours 4 minutes" in result.output


def test_short_duration_no_spaces():
    runner = CliRunner()
    result = runner.invoke(cli, ["--duration", "3d2m"])
    assert result.exit_code == CLICK_SUCCESS
    assert "Duration: 3 days 2 minutes" in result.output


def test_invalid_duration():
    runner = CliRunner()
    result = runner.invoke(cli, ["--duration", "invalid-duration"])
    assert result.exit_code != CLICK_SUCCESS
    assert "Invalid value for '--duration'" in result.output
