import pytest
import click
from click.testing import CliRunner
import pendulum

# Assuming your click date time type is defined in a module named click_datetime
from click_datetime import ClickDateTimeType

@click.command()
@click.option('--date', type=ClickDateTimeType())
def cli(date):
    click.echo(f"Date: {date}")

def test_valid_date():
    runner = CliRunner()
    result = runner.invoke(cli, ['--date', '2024-09-10'])
    assert result.exit_code == 0
    assert "Date: 2024-09-10T00:00:00" in result.output

def test_invalid_date():
    runner = CliRunner()
    result = runner.invoke(cli, ['--date', 'invalid-date'])
    assert result.exit_code != 0
    assert "Invalid value for '--date'" in result.output

def test_valid_datetime():
    runner = CliRunner()
    result = runner.invoke(cli, ['--date', '2024-09-10T15:30:00'])
    assert result.exit_code == 0
    assert "Date: 2024-09-10T15:30:00" in result.output

def test_invalid_datetime_format():
    runner = CliRunner()
    result = runner.invoke(cli, ['--date', '2024/09/10'])
    assert result.exit_code != 0
    assert "Invalid value for '--date'" in result.output
