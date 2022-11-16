import led_control

led_control.color_pwm_set(0, 0, 100)
import connect
import home_time

led_control.color_pwm_set(0, 100, 0)

from machine import Timer, Pin

heartbeat_led = Pin("LED", Pin.OUT)


def heartbeat(_):
    heartbeat_led.toggle()


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


heartbeat_timer = Timer()
heartbeat_timer.init(freq=1, mode=Timer.PERIODIC, callback=heartbeat)

led_check_timer = Timer()
led_check_timer.init(freq=3, mode=Timer.PERIODIC, callback=led_check)
