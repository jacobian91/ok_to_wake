import network
import time
import credentials

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Wait for connect or fail
while True:
    wlan.connect(credentials.wifi_ssid, credentials.wifi_pass)
    while True:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        print("waiting for connection...")
        time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        print("connection failed")
        continue
        raise RuntimeError("network connection failed")
    else:
        print("connected")
        status = wlan.ifconfig()
        print("ip = " + status[0])
        break
