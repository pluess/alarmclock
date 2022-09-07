import time

class WlanConnector:

    def __init__(self, network, retries: int = 10) -> None:
        self.retries = retries
        self.network = network

    def connect(self, ssid : str, password : str):
        wlan = self.network.WLAN(self.network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        max_wait = self.retries
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print('waiting for WLAN connection...')
            time.sleep(1)

        if wlan.status() != 3:
            raise RuntimeError('WLAN connection failed')
        else:
            print('WLAN connected')
            status = wlan.ifconfig()
            print( 'ip = ' + status[0] )