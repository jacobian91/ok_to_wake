import network
import time
import credentials

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(credentials.wifi_ssid, credentials.wifi_pass)

# Wait for connect or fail
while True:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    print("waiting for connection...")
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError("network connection failed")
else:
    print("connected")
    status = wlan.ifconfig()
    print("ip = " + status[0])