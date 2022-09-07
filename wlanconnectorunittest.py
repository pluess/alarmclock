import unittest
from wlanconnector import WlanConnector

class WlanMock:

    def __init__(self) -> None:
        pass

    def active(self, somIgnoredValue : bool):
        pass

    def connect(self, ignoredSsid : str, ingoredPw : str):
        pass

    def status(self) -> int:
        return 1

    def ifconfig(self):
        return ('99.99.99.99')

class StatefulWlanMock(WlanMock):

    def __init__(self) -> None:
        self.statusCallCounter = 0


    def status(self) -> int:
        if self.statusCallCounter < 3:
            self.statusCallCounter += self.statusCallCounter + 1
            return 1
        else: return 3

class NetworkMock:

    def __init__(self, wlanMock) -> None:
        self.STA_IF = 'dummy value'
        self.wlanMock = wlanMock

    def WLAN(self, ignoredDummyValue) -> WlanMock:
     return self.wlanMock
 

class WlanConnectorUnitTest(unittest.TestCase):

    def test_no_connection(self):
        network = NetworkMock(WlanMock())
        wlanConnectort = WlanConnector(network, 2)
        try:
            wlanConnectort.connect('someSsid', 'somePw')
            self.fail('Shuld raise RuntimeError')
        except RuntimeError:
            pass

    def test_connection(self):
        network = NetworkMock(StatefulWlanMock())
        wlanConnectort = WlanConnector(network, 3)
        wlanConnectort.connect('someSsid', 'somePw')

if __name__ == '__main__':  # type: ignore
    unittest.main()