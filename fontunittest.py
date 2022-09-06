import unittest
from font import Font
from font import chunker

font_numbers8x6 = [
  0x04, 0x0a, 0x11, 0x11, 0x11, 0x11, 0x0a, 0x04, 
  0x04, 0x0c, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0e, 
  0x0e, 0x11, 0x01, 0x06, 0x08, 0x10, 0x10, 0x1f, 
]

def mapCharacters(characterList: dict)-> dict:
	characterDict = {}
	characterDict['1'] = characterList[0]
	characterDict['2'] = characterList[1]
	characterDict['3'] = characterList[2]
	return characterDict

class FontUnitTest(unittest.TestCase):

	def setUp(self):
		self.font = Font(font_numbers8x6, 6, 8, mapCharacters, True)  # type: ignore

	def test_chunker(self):
		seq = [1,2,3,4,5,6,7,8,9,10]
		expectedSeqSeq = [[1,2,3,4,5],[6,7,8,9,10]]

		actualSeqSeq = chunker(seq, 5)
		self.assertEqual(expectedSeqSeq[0], next(actualSeqSeq))
		self.assertEqual(expectedSeqSeq[1], next(actualSeqSeq))

	def test_toCharField(self):
		a =  self.font.toCharField(0b010101)
		self.assertEqual(a, '..XX..XX..XX')
		a =  self.font.toCharField(0b101010)
		self.assertEqual(a, 'XX..XX..XX..')
		a =  self.font.toCharField(0b000000)
		self.assertEqual(a, '............')
		a =  self.font.toCharField(0b111111)
		self.assertEqual(a, 'XXXXXXXXXXXX')

	def test_toBinaryString(self):
		a =  self.font.toBinaryString(0b010101)
		self.assertEqual(a, '010101')
		a =  self.font.toBinaryString(0b101010)
		self.assertEqual(a, '101010')
		a =  self.font.toBinaryString(0b000000)
		self.assertEqual(a, '000000')
		a =  self.font.toBinaryString(0b111111)
		self.assertEqual(a, '111111')

	def test_getitem_int(self):
		actualCharacter = self.font[1]
		expectedCharacter = [ 0x04, 0x0c, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0e ]
		self.assertEqual(actualCharacter, expectedCharacter)

	def test_getitem_symbolic(self):
		actualCharacter = self.font['2']
		expectedCharacter = [ 0x04, 0x0c, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0e ]
		self.assertEqual(actualCharacter, expectedCharacter)

if __name__ == '__main__':
	unittest.main()