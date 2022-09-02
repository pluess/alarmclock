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
		a =  self.c64German.toCharField(0b01010101)
		self.assertEqual(a, '..XX..XX..XX..XX')
		a =  self.c64German.toCharField(0b10101010)
		self.assertEqual(a, 'XX..XX..XX..XX..')
		a =  self.c64German.toCharField(0b00000000)
		self.assertEqual(a, '................')
		a =  self.c64German.toCharField(0b11111111)
		self.assertEqual(a, 'XXXXXXXXXXXXXXXX')

if __name__ == '__main__':  # type: ignore
	unittest.main()