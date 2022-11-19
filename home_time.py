import time

import ntptime
import urequests as requests

try:  # Type checking
    import typing

    if typing.TYPE_CHECKING:
        from typing import Dict

        import requests
except:
    pass

TIME_NAMES = ["year", "day", "month", "hour", "min", "sec", "ms"]

local_details: Dict[str, float] = {"last_sync": 0, "offset": 0}
TWLEVE_HOURS = 12 * 60 * 60

initialized_time = {"status": False}


def get_home_time() -> Dict[str, int]:
    if time.time() - TWLEVE_HOURS > local_details["last_sync"]:
        try:
            print("New Time Sync")
            ntptime.settime()
            initialized_time["status"] = True
            local_details["last_sync"] = time.time()
            response = requests.get(
                "http://worldtimeapi.org/api/timezone/America/Los_Angeles"
            ).json()
            local_details["offset"] = response["raw_offset"]
            unixtime = response["unixtime"]
        except Exception as exc:
            if initialized_time["status"]:
                pass  # Was initialized once, trust current RTC for now
            else:
                raise exc
    else:
        unixtime = time.time()

    home_time: tuple = time.localtime(unixtime + local_details["offset"])
    return dict(zip(TIME_NAMES, home_time))
