import application 

import unittest
from display import Display

class TimeMock:

    def localtime(self):
        return (2022, 9, 8, 1, 2, 3, 9, 9)

class DisplayUnitTest(unittest.TestCase):

    def setUp(self):
        self.display = Display(TimeMock(), None)  # type: ignore

    def test_getTimeStrings(self):
        hours, minutes = self.display.getTimeStrings()
        self.assertEqual(hours, '01')
        self.assertEqual(minutes, '02')

if __name__ == '__main__':  # type: ignore
    unittest.main()