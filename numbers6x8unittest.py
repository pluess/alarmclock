import unittest
from numbers6x8 import Numbers6x8
from numbers6x8 import mapCharacters

class C64GermanUnitTest(unittest.TestCase):

	def setUp(self):
		self.c64German = Numbers6x8(True)

	def test_getitem_int(self):
		actualCharacter = self.c64German[5]
		expectedCharacter = [31, 16, 16, 30, 1, 1, 17, 14]
		self.assertEqual(actualCharacter, expectedCharacter)

	def test_getitem_symbolic(self):
		actualCharacter = self.c64German['5']
		expectedCharacter = [31, 16, 16, 30, 1, 1, 17, 14]
		self.assertEqual(actualCharacter, expectedCharacter)

	def test_mapCharacters(self):
		actualCharacterDict = mapCharacters(self.c64German.numericCharacterList)
		self.assertEqual(actualCharacterDict['1'], [4, 12, 4, 4, 4, 4, 4, 14])
		self.assertEqual(actualCharacterDict['9'], [14, 17, 17, 15, 1, 1, 2, 12])
		self.assertEqual(actualCharacterDict['colon'], [0, 12, 12, 0, 0, 12, 12, 0])

if __name__ == '__main__':  # type: ignore
	unittest.main()