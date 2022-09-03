import unittest
from c64german import C64German

class C64GermanUnitTest(unittest.TestCase):

	def setUp(self):
		self.c64German = C64German()

	def test_chunker(self):
		seq = [1,2,3,4,5,6,7,8,9,10]
		expectedSeqSeq = [[1,2,3,4,5],[6,7,8,9,10]]

		actualSeqSeq = self.c64German.chunker(seq, 5)
		self.assertEqual(expectedSeqSeq[0], next(actualSeqSeq))  # type: ignore
		self.assertEqual(expectedSeqSeq[1], next(actualSeqSeq))  # type: ignore

	def test_toCharField(self):
		a =  self.c64German.toCharField(0b01010101)  # type: ignore
		self.assertEqual(a, '..XX..XX..XX..XX')
		a =  self.c64German.toCharField(0b10101010)  # type: ignore
		self.assertEqual(a, 'XX..XX..XX..XX..')
		a =  self.c64German.toCharField(0b00000000)  # type: ignore
		self.assertEqual(a, '................')
		a =  self.c64German.toCharField(0b11111111)  # type: ignore
		self.assertEqual(a, 'XXXXXXXXXXXXXXXX')

	def test_getitem_int(self):
		actualCharacter = self.c64German[129]
		expectedCharacter = [231, 195, 153, 153, 129, 153, 153, 255]
		self.assertEqual(actualCharacter, expectedCharacter)

	def test_getitem_symbolic(self):
		actualCharacter = self.c64German['A']
		expectedCharacter = [24, 60, 102, 102, 126, 102, 102, 0]
		self.assertEqual(actualCharacter, expectedCharacter)

	def test_mapCharacters(self):
		actualCharacterDict = self.c64German.mapCharacters(self.c64German.numericCharacterList)
		self.assertEqual(actualCharacterDict['A'], [24, 60, 102, 102, 126, 102, 102, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['Z'], [126, 6, 12, 24, 48, 96, 126, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['a'], [0, 0, 60, 6, 62, 102, 62, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['z'], [0, 0, 126, 12, 24, 48, 126, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['0'], [60, 102, 110, 118, 102, 102, 60, 0])  # type: ignore
		self.assertEqual(actualCharacterDict['9'], [60, 102, 102, 62, 6, 102, 60, 0])  # type: ignore

if __name__ == '__main__':  # type: ignore
	unittest.main()