from machine import Pin, PWM

pwm_r = PWM(Pin(17))
pwm_g = PWM(Pin(18))
pwm_b = PWM(Pin(19))

PWM_100_U16 = 65535
PWM_FREQ = 500

pwm_r.freq(PWM_FREQ)
pwm_g.freq(PWM_FREQ)
pwm_b.freq(PWM_FREQ)


def color_pwm_set(r, g, b):
    pwm_r.duty_u16(int(r * PWM_100_U16 / 100))
    pwm_g.duty_u16(int(g * PWM_100_U16 / 100))
    pwm_b.duty_u16(int(b * PWM_100_U16 / 100))
