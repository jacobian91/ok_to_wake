import time

import urequests as requests

# import ntptime

try:  # Type checking
    import typing

    if typing.TYPE_CHECKING:
        from typing import Dict
        import requests
except:
    pass

# ntptime.settime()
TIME_NAMES = ["year", "day", "month", "hour", "min", "sec", "ms"]


def get_home_time() -> Dict[str, int]:
    response = requests.get(
        "http://worldtimeapi.org/api/timezone/America/Los_Angeles"
    ).json()

    home_time: tuple = time.localtime(response["unixtime"] + response["raw_offset"])
    return dict(zip(TIME_NAMES, home_time))
