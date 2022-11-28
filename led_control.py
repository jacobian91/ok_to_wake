from machine import PWM, Pin, Timer
import time

PWM_100_U16 = 65535
PWM_FREQ = 500

heartbeat_led = Pin("LED", Pin.OUT)
heartbeat_timer = Timer()

pwm_r = PWM(Pin(17))
pwm_g = PWM(Pin(18))
pwm_b = PWM(Pin(19))

pwm_r.freq(PWM_FREQ)
pwm_g.freq(PWM_FREQ)
pwm_b.freq(PWM_FREQ)

RED = (100, 0, 0, "RED")
GREEN = (0, 100, 0, "GREEN")
DIMGREEN = (0, 60, 0, "DIM GREEN")
BLUE = (0, 0, 100, "BLUE")
WHITE = (100, 100, 100, "WHITE")
BLUEGREEN = (0, 100, 100, "BLUE GREEN")
PURPLE = (100, 0, 100, "PURPLE")
YELLOW = (100, 20, 0, "YELLOW")
DIMWHITE = (10, 10, 10, "DIM WHITE")

current_led_setting = (0, 0, 0, "OFF")


def color_pwm_set(r, g, b, color_name=None):
    global current_led_setting
    if (r, g, b, color_name) == current_led_setting:
        print(f"No Change to LED needed, keeping as: {color_name}")
        return
    print(f"Setting Color to: {color_name} from {current_led_setting[3]}")
    current_led_setting = (r, g, b, color_name)
    pwm_r.duty_u16(int(r * PWM_100_U16 / 100))
    pwm_g.duty_u16(int(g * PWM_100_U16 / 100))
    pwm_b.duty_u16(int(b * PWM_100_U16 / 100))


def heartbeat(timer_param=None):
    heartbeat_led.on()
    time.sleep(0.001)
    heartbeat_led.off()


def run_heartbeat(period: int):
    heartbeat_timer.init(period=period, mode=Timer.PERIODIC, callback=heartbeat)
