import time
from logutil import get_logger

class WlanConnector:

    def __init__(self, network, retries: int = 10) -> None:
        self.retries = retries
        self.network = network
        self.logger = get_logger(__name__)

    def connect(self, ssid : str, password : str):
        wlan = self.network.WLAN(self.network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)

        max_wait = self.retries
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            self.logger.info('waiting for WLAN connection...')
            time.sleep(1)

        if wlan.status() != 3:
            raise RuntimeError('WLAN connection failed')
        else:
            self.logger.info('WLAN connected')
            status = wlan.ifconfig()
            self.logger.info( 'ip = ' + status[0] )