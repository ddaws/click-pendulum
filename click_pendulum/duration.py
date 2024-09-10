import click
import pendulum


class Duration(click.ParamType):
    """
    A Pendulum Duration object
    """

    name = "duration"

    _pattern: str

    def __init__(self, pattern: str):
        self._pattern = pattern

    def convert(self, value: str | None, param, ctx):
        import re
        if value is None:
            return value

        try:
            match = re.match(self._pattern, value)
            if not match:
                raise ValueError("Invalid duration format")

            duration_kwargs = {
                "weeks": int(match.group("weeks") or 0),
                "days": int(match.group("days") or 0),
                "hours": int(match.group("hours") or 0),
                "minutes": int(match.group("minutes") or 0),
                "seconds": int(match.group("seconds") or 0),
            }

            return pendulum.duration(**duration_kwargs)
        except ValueError as ex:
            self.fail(
                f'Could not parse duration string "{value}" ({ex})',
                param,
                ctx,
            )
