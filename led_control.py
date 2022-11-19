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

RED = (100, 0, 0)
GREEN = (0, 100, 0)
DIMGREEN = (0, 60, 0)
BLUE = (0, 0, 100)
WHITE = (100, 100, 100)
BLUEGREEN = (0, 100, 100)
PURPLE = (100, 0, 100)
YELLOW = (100, 20, 0)
DIMWHITE = (10, 10, 10)


def color_pwm_set(r, g, b):
    pwm_r.duty_u16(int(r * PWM_100_U16 / 100))
    pwm_g.duty_u16(int(g * PWM_100_U16 / 100))
    pwm_b.duty_u16(int(b * PWM_100_U16 / 100))


def heartbeat(_):
    heartbeat_led.on()
    time.sleep(0.001)
    heartbeat_led.off()


def run_heartbeat(period: int):
    heartbeat_timer.init(period=period, mode=Timer.PERIODIC, callback=heartbeat)
