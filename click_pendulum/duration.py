import click
import pendulum


class Duration(click.ParamType):
    """
    A Pendulum Duration object
    """

    name = "duration"

    def convert(self, value: str | None, param, ctx):
        if value is None:
            return value

        try:
            return pendulum.parse(value).diff()
        except ValueError as ex:
            self.fail(
                f'Could not parse duration string "{value}" ({ex})',
                param,
                ctx,
            )
