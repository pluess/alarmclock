import application

import unittest
from brightness import Brightness

class LdrMock:

    def __init__(self, readValue : int = 1) -> None:
        self.readValue = readValue

    def read_sensor(self) -> int:
        return self.readValue

class BrightnessUnitTest(unittest.TestCase):

    def test_getCurrentBrighness(self):
        testTupples = (
            (15000, 5),
            (58400, 200),
            (36700, 102)
        )
        for actualLdr, expectedBrightness in testTupples:
            brightness = Brightness(LdrMock(actualLdr))
            actualBrightness = brightness.getCurrentBrightness()
            self.assertEqual(actualBrightness, expectedBrightness)


if __name__ == '__main__':  # type: ignore
    unittest.main()
