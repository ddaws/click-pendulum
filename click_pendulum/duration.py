import re

import click
import pendulum


class Duration(click.ParamType):
    """
    A Pendulum Duration object.

    The pattern used for matching must include the following named groups:
    - weeks: Matches the number of weeks.
    - days: Matches the number of days.
    - hours: Matches the number of hours.
    - minutes: Matches the number of minutes.
    - seconds: Matches the number of seconds.

    Each group is optional, but the pattern must be structured to capture these groups if present.
    """

    name = "duration"

    DEFAULT_PATTERN = r"(?:(?P<weeks>\d+)\s*w(?:eeks?)?)?\s*(?:(?P<days>\d+)\s*d(?:ays?)?)?\s*(?:(?P<hours>\d+)\s*h(?:ours?)?)?\s*(?:(?P<minutes>\d+)\s*m(?:inutes?)?)?\s*(?:(?P<seconds>\d+)\s*s(?:econds?)?)?"

    _pattern: re.Pattern

    def __init__(self, pattern: str = DEFAULT_PATTERN):
        self._pattern = re.compile(pattern)

    def convert(self, value: str | None, param, ctx):
        if value is None:
            return value

        try:
            match = self._pattern.match(value)
            if not match or not match.group(0).strip():
                raise ValueError("Invalid duration format: no matches found")

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
