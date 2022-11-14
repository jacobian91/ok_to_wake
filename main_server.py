try:
    import usocket as socket
except:
    import socket

response_template = """HTTP/1.0 200 OK

%s
"""
import machine
import utime
import urequests

RESPONSE_404 = "HTTP/1.0 404 NOT FOUND\n\n<h1>404 Not Found</h1>"
RESPONSE_500 = (
    "HTTP/1.0 500 INTERNAL SERVER ERROR\n\n<h1>500 Internal Server Error</h1>"
)
REFRESH_BODY = '<html><meta http-equiv="refresh" content=".5" > %s </html>'

MY_TIME_URL = "https://guarded-forest-56274.herokuapp.com/"
ESPLED = machine.Pin(16, machine.Pin.OUT)
EXTERNAL_LED = machine.Pin(10, machine.Pin.OUT)
SWITCH_PIN = machine.Pin(5, machine.Pin.IN)

adc = machine.ADC(0)
pwm = machine.Pin(14)
pwm = machine.PWM(pwm)


def time():
    mytime = urequests.request("GET", MY_TIME_URL)
    body = "Current Time is: %s" % mytime.content
    body = REFRESH_BODY % body
    return response_template % body


def dummy():
    body = "This is a dummy endpoint"

    return response_template % body


def light_on():
    EXTERNAL_LED.value(1)
    body = "You turned a light on!"
    return response_template % body


def light_off():
    EXTERNAL_LED.value(0)
    body = "You turned a light off!"
    return response_template % body


def switch():
    body = "State of switch: %d" % SWITCH_PIN.value()
    body = REFRESH_BODY % body
    return response_template % body


def light():
    value = adc.read()
    color = hex(255 - value)[2:] * 3
    bg_color_tag = '<body style="background-color:#%s;">' % color
    body = "Value of Photoresistor ADC: %f" % value
    body = bg_color_tag + body + "</body>"
    body = REFRESH_BODY % body
    return response_template % body


def sweep():
    for i in range(0, 1000, 10):
        utime.sleep(0.02)
        pwm.duty(i)
    body = "Sweep Complete"
    body = REFRESH_BODY % body
    return response_template % body

def speaker():
    pwm = machine.PWM(machine.Pin(14),duty=512)
    for i in range(0, 1000, 10):
        utime.sleep(0.05)
        pwm.freq(i)
    pwm.deinit()
    body = "Sweep Complete"
    body = REFRESH_BODY % body
    return response_template % body

handlers = {
    "time": time,
    "dummy": dummy,
    "light_on": light_on,
    "light_off": light_off,
    "switch": switch,
    "light": light,
    "sweep": sweep,
    "speaker": speaker,
}


def main():
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", 8080)
    addr = ai[0][-1]
    led_state = True

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://<this_host>:8080/")
    ESPLED.value(1)

    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        req = client_s.recv(4096)

        # Flash LED when connecting
        ESPLED.value(0)

        print("Request:")
        print(req)

        try:
            path = req.decode().split("\r\n")[0].split(" ")[1]
            handler = handlers[path.strip("/").split("/")[0]]
            response = handler()
        except KeyError:
            response = RESPONSE_404
        except Exception:
            response = RESPONSE_500

        # A handler returns an entire response in the form of a multi-line string.
        # This breaks up the response into single strings, byte-encodes them, and
        # joins them back together with b"\r\n". Then it sends that to the client.
        client_s.send(b"\r\n".join([line.encode() for line in response.split("\n")]))

        client_s.close()
        print()
        ESPLED.value(1)


main()
