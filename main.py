from machine import Timer, reset

import led_control
import logger

led_control.color_pwm_set(*led_control.BLUE)
led_control.run_heartbeat(period=200)
import connect

connect.reconnect()
import home_time
from webrepl import webrepl

webrepl.start()

led_control.run_heartbeat(period=4000)
led_control.color_pwm_set(*led_control.WHITE)

LIGHT_TIMES = [
    (1700, led_control.RED),
    (745, led_control.DIMWHITE),
    (630, led_control.GREEN),
    (500, led_control.YELLOW),
    (0, led_control.RED),
]


def led_check(timer_param=None):
    try:
        current_time = home_time.get_home_time()
    except OSError:
        return  # Failed to get time, try again next time this is called
    time_s = [f"{name}={current_time[name]}" for name in home_time.TIME_NAMES]
    time_s = " ".join(time_s)
    print(time_s)
    current_hour_min = current_time["hour"] * 100 + current_time["min"]
    for light_time, light_color in LIGHT_TIMES:
        if current_hour_min >= light_time:
            led_control.color_pwm_set(*light_color)
            break


led_check()  # Set immediatly instead of waiting for timer
led_check_timer = Timer()
led_check_timer.init(period=20000, mode=Timer.PERIODIC, callback=led_check)


def stop():
    "Stops all timers, helper function to keep REPL clean."
    led_check_timer.deinit()
    led_control.heartbeat_timer.deinit()
    connect.connection_timer.deinit()
