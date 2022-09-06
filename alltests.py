import unittest
from c64germanunittest import C64GermanUnitTest
from coordinatesunittest import CooridnatesUnitTest
from fontunittest import FontUnitTest
from neodrawunittest import NeoDrawUnitTest
from numbers6x8unittest import Numbers6x8UnitTest

suite = unittest.TestSuite()

#suite.addTest(C64GermanUnitTest)
suite.addTest(CooridnatesUnitTest)
suite.addTest(FontUnitTest)
suite.addTest(NeoDrawUnitTest)
suite.addTest(Numbers6x8UnitTest)

runner = unittest.TestRunner()
runner.run(suite)