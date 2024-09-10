import click
import pendulum

from click_pendulum import Duration


@click.command()
@click.option("--duration", type=Duration(), help="Parse a duration string.")
def cli(duration: pendulum.Duration):
    click.echo(f"Duration: {duration}")


if __name__ == "__main__":
    cli()  # type: ignore
