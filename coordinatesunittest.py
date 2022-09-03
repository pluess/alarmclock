import unittest
from coordinates import Cooridnates

class CooridnatesUnitTest(unittest.TestCase):

	def setUp(self):
		self.coordinates = Cooridnates(256, 8)

	def test_chunker(self):
		self.assertEqual(self.coordinates.cartesianToPostion(31, 0), 0)
		self.assertEqual(self.coordinates.cartesianToPostion(31, 1), 1)
		self.assertEqual(self.coordinates.cartesianToPostion(31, 2), 2)
		self.assertEqual(self.coordinates.cartesianToPostion(31, 7), 7)

		self.assertEqual(self.coordinates.cartesianToPostion(30, 0), 15)
		self.assertEqual(self.coordinates.cartesianToPostion(30, 1), 14)
		self.assertEqual(self.coordinates.cartesianToPostion(30, 2), 13)
		self.assertEqual(self.coordinates.cartesianToPostion(30, 7), 8)

		self.assertEqual(self.coordinates.cartesianToPostion(29, 0), 16)
		self.assertEqual(self.coordinates.cartesianToPostion(29, 1), 17)
		self.assertEqual(self.coordinates.cartesianToPostion(29, 2), 18)
		self.assertEqual(self.coordinates.cartesianToPostion(29, 7), 23)
  
		self.assertEqual(self.coordinates.cartesianToPostion(2, 0), 239)
		self.assertEqual(self.coordinates.cartesianToPostion(2, 1), 238)
		self.assertEqual(self.coordinates.cartesianToPostion(2, 2), 237)
		self.assertEqual(self.coordinates.cartesianToPostion(2, 7), 232)

		self.assertEqual(self.coordinates.cartesianToPostion(1, 0), 240)
		self.assertEqual(self.coordinates.cartesianToPostion(1, 1), 241)
		self.assertEqual(self.coordinates.cartesianToPostion(1, 2), 242)
		self.assertEqual(self.coordinates.cartesianToPostion(1, 7), 247)

		self.assertEqual(self.coordinates.cartesianToPostion(0, 0), 255)
		self.assertEqual(self.coordinates.cartesianToPostion(0, 1), 254)
		self.assertEqual(self.coordinates.cartesianToPostion(0, 2), 253)
		self.assertEqual(self.coordinates.cartesianToPostion(0, 7), 248)
  
if __name__ == '__main__':  # type: ignore
	unittest.main()