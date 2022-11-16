from machine import Timer

import led_control

led_control.color_pwm_set(0, 0, 100)  # Blue
led_control.run_heartbeat(period=10)
import connect
import home_time

led_control.run_heartbeat(period=1000)
led_control.color_pwm_set(0, 100, 0)  # Green


def led_check(_):
    current_time = home_time.get_home_time()
    print(current_time["sec"])
    if current_time["sec"] > 45:
        led_control.color_pwm_set(100, 0, 0)
    elif current_time["sec"] > 30:
        led_control.color_pwm_set(0, 100, 0)
    elif current_time["sec"] > 15:
        led_control.color_pwm_set(0, 0, 100)
    else:
        led_control.color_pwm_set(100, 100, 100)


led_check_timer = Timer()
led_check_timer.init(period=3000, mode=Timer.PERIODIC, callback=led_check)
