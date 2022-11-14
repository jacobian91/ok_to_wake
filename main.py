import machine
import time

LATCH = machine.Pin(16, machine.Pin.OUT)
SHIFT = machine.Pin(5, machine.Pin.OUT)
SERIAL = machine.Pin(10, machine.Pin.OUT)

LATCH.value(0)
SHIFT.value(0)
SERIAL.value(0)

TIME_FLIP = 0.002
TIME_ANIM = 0.1

def reset_register():
    set_register('0'*8)

def set_register(output):
    LATCH.value(0)
    for value in output:
        SERIAL.value(int(value))
        time.sleep(TIME_FLIP)
        SHIFT.value(1)
        time.sleep(TIME_FLIP)
        SHIFT.value(0)
        time.sleep(TIME_FLIP)
    LATCH.value(1)
    time.sleep(TIME_FLIP)
    LATCH.value(0)

def scan():
    for i in range(16):
        time.sleep(TIME_ANIM)
        register = ['0']*8
        if i <=7:
            register[i] = '1'
        else:
            register[15-i] = '1'
        set_register(''.join(register))


def main():
    reset_register()
    scan()

main()
