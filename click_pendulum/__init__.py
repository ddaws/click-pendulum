import click
import pendulum
from pendulum import UTC, Timezone


class DateTime(click.ParamType):
    """
    A Pendulum DateTime object
    """

    name = "date"

    _format: str
    _tz: Timezone

    def __init__(self, format: str, tz: Timezone = UTC):
        self._format = format
        self._tz = tz

    def convert(self, value: str | None, param, ctx):
        if value is None:
            return value

        if isinstance(value, DateTime):
            return value

        try:
            return pendulum.from_format(value, self._format, self._tz)
        except ValueError as ex:
            self.fail(
                'Could not parse datetime string "{datetime_str}" formatted as {format} ({ex})'.format(
                    datetime_str=value,
                    format=self._format,
                    ex=ex,
                ),
                param,
                ctx,
            )
