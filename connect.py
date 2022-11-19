import network
import time
import credentials

wlan = network.WLAN(network.STA_IF)
wlan.active(True)


class WLAN_STATUSES:
    STAT_WRONG_PASSWORD = -3
    STAT_NO_AP_FOUND = -2
    STAT_CONNECT_FAIL = -1
    STAT_IDLE = 0
    STA_IF = 0
    AP_IF = 1
    UNKNOWN = 2
    STAT_CONNECTING = 1
    STAT_GOT_IP = 3


# Wait for connect or fail
def reconnect():
    while True:
        wlan.connect(credentials.wifi_ssid, credentials.wifi_pass)
        while True:
            time.sleep(1)
            status = wlan.status()
            print(f"Network Status={status}")
            if status == WLAN_STATUSES.STAT_GOT_IP:
                config = wlan.ifconfig()
                print("Connected IP = " + config[0])
                return
            elif status == WLAN_STATUSES.STAT_CONNECTING:
                print("Waiting for Connection...")
                continue
            else:
                print("Connection Failed")
                break
