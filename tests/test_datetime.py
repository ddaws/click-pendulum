import click
import pendulum
import pytest
from click.testing import CliRunner

# Assuming your click date time type is defined in a module named click_datetime
from click_pendulum import DateTime

CLICK_SUCCESS = 0


@click.command()
@click.option("--date", type=DateTime())
def cli(date: pendulum.DateTime):
    assert isinstance(date, pendulum.DateTime)
    click.echo(f"Date: {date}")


def test_valid_date():
    runner = CliRunner()
    result = runner.invoke(cli, ["--date", "2024-09-10"])
    assert result.exit_code == CLICK_SUCCESS
    assert "Date: 2024-09-10 00:00:00" in result.output


def test_invalid_date():
    runner = CliRunner()
    result = runner.invoke(cli, ["--date", "invalid-date"])
    assert result.exit_code != CLICK_SUCCESS
    assert "Invalid value for '--date'" in result.output


def test_valid_datetime():
    runner = CliRunner()
    result = runner.invoke(cli, ["--date", "2024-09-10T15:30:00"])
    assert result.exit_code == CLICK_SUCCESS
    assert "Date: 2024-09-10 15:30:00" in result.output


def test_invalid_datetime_format():
    runner = CliRunner()
    result = runner.invoke(cli, ["--date", "2024/09/10"])
    assert result.exit_code == CLICK_SUCCESS
    assert "Date: 2024-09-10 00:00:00" in result.output
