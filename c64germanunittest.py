import unittest
from c64german import C64German
from c64german import mapCharacters

class C64GermanUnitTest(unittest.TestCase):

	def setUp(self):
		self.c64German = C64German()

	def test_getitem_int(self):
		actualCharacter = self.c64German[129]
		expectedCharacter = [231, 195, 153, 153, 129, 153, 153, 255]
		self.assertEqual(actualCharacter, expectedCharacter)

	def test_getitem_symbolic(self):
		actualCharacter = self.c64German['A']
		expectedCharacter = [24, 60, 102, 102, 126, 102, 102, 0]
		self.assertEqual(actualCharacter, expectedCharacter)

	def test_mapCharacters(self):
		actualCharacterDict = mapCharacters(self.c64German.numericCharacterList)
		self.assertEqual(actualCharacterDict['A'], [24, 60, 102, 102, 126, 102, 102, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['Z'], [126, 6, 12, 24, 48, 96, 126, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['a'], [0, 0, 60, 6, 62, 102, 62, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['z'], [0, 0, 126, 12, 24, 48, 126, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['0'], [60, 102, 110, 118, 102, 102, 60, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['9'], [60, 102, 102, 62, 6, 102, 60, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['colon'], [0, 0, 24, 0, 0, 24, 0, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['heart'], [54, 127, 127, 127, 62, 28, 8, 0])  # type: ignore

if __name__ == '__main__':  # type: ignore
	unittest.main()