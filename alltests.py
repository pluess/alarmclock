import application 

import unittest
from c64germanunittest import C64GermanUnitTest
from coordinatesunittest import CooridnatesUnitTest
from fontunittest import FontUnitTest
from neodrawunittest import NeoDrawUnitTest
from numbers6x8unittest import Numbers6x8UnitTest
from wlanconnectorunittest import WlanConnectorUnitTest
from worldtimeapiunittest import WorldTimeApiUnitTest

suite = unittest.TestSuite()

suite.addTest(C64GermanUnitTest)  # type: ignore
suite.addTest(CooridnatesUnitTest)  # type: ignore
suite.addTest(FontUnitTest)  # type: ignore
suite.addTest(NeoDrawUnitTest)  # type: ignore
suite.addTest(Numbers6x8UnitTest)  # type: ignore
suite.addTest(WlanConnectorUnitTest)  # type: ignore
suite.addTest(WorldTimeApiUnitTest)  # type: ignore

runner = unittest.TestRunner()  # type: ignore
runner.run(suite)