# Click Pendulum

Click support for Pendulum date, time, interval and duration types to allow 
developers to easily parse strings as parameters to Python click CLIs.

## Example

You can accept a Pendulum DateTime as a parameter to your click CLI

```python
import click, pendulum
from click_pendulum import DateTime


@click.option(
    "--date",
    type=DateTime(),
    default=pendulum.now(),
    help="An example parsing and printing a datetime.",
)
@click.command()
def cli(date: pendulum.DateTime):
    click.echo("The date : {0}".format(date))


if __name__ == "__main__":
    cli()  # type: ignore
```

```bash
$ python main.py --date=2016-01-01
```

## Installation

```bash
pip install click-pendulum
```

## Development

### Building and packaging

```bash
poetry build
```

### Testing the compiled wheel

```bash
# Create a virtual environment for testing
python -m .venv/test
source .venv/test/bin/activate

# Confirm importing and exporting is correct
python -c 'import click_pendulum as cd; print(dir(cd))'
```

## Authors

- Dawson Reid (@ddaws)
