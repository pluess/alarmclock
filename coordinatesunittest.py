import unittest
from coordinates import Cooridnates

"""
3x3
===
! 08  03 ---- 02
! 07  04 !  ! 01
! 06  05 !  ! 00
----------

4*3
===
09 ---- 08  03 ---- 02
10 !  ! 07  04 !  ! 01
11 !  ! 06  05 !  ! 00
      ----------
"""
class CooridnatesUnitTest(unittest.TestCase):

	def test_cartesianToPostion_Square_3_3(self):
		coordinates = Cooridnates(9, 3)
		self.assertEqual(coordinates.cartesianToPostion(0, 0), 6)
		self.assertEqual(coordinates.cartesianToPostion(1, 0), 5)
		self.assertEqual(coordinates.cartesianToPostion(2, 0), 0)

		self.assertEqual(coordinates.cartesianToPostion(0, 1), 7)
		self.assertEqual(coordinates.cartesianToPostion(1, 1), 4)
		self.assertEqual(coordinates.cartesianToPostion(2, 1), 1)

		self.assertEqual(coordinates.cartesianToPostion(0, 2), 8)
		self.assertEqual(coordinates.cartesianToPostion(1, 2), 3)
		self.assertEqual(coordinates.cartesianToPostion(2, 2), 2)

	def test_cartesianToPostion_Square_4_3(self):
		coordinates = Cooridnates(12, 3)
		self.assertEqual(coordinates.cartesianToPostion(0, 0),11)
		self.assertEqual(coordinates.cartesianToPostion(1, 0), 6)
		self.assertEqual(coordinates.cartesianToPostion(2, 0), 5)
		self.assertEqual(coordinates.cartesianToPostion(3, 0), 0)

		self.assertEqual(coordinates.cartesianToPostion(0, 1),10)
		self.assertEqual(coordinates.cartesianToPostion(1, 1), 7)
		self.assertEqual(coordinates.cartesianToPostion(2, 1), 4)
		self.assertEqual(coordinates.cartesianToPostion(3, 1), 1)

		self.assertEqual(coordinates.cartesianToPostion(0, 2), 9)
		self.assertEqual(coordinates.cartesianToPostion(1, 2), 8)
		self.assertEqual(coordinates.cartesianToPostion(2, 2), 3)
		self.assertEqual(coordinates.cartesianToPostion(3, 2), 2)

	def test_cartesianToPostion_BigMatrix(self):
		coordinates = Cooridnates(256, 8)
		self.assertEqual(coordinates.cartesianToPostion(31, 0), 0)
		self.assertEqual(coordinates.cartesianToPostion(31, 1), 1)
		self.assertEqual(coordinates.cartesianToPostion(31, 2), 2)
		self.assertEqual(coordinates.cartesianToPostion(31, 7), 7)

		self.assertEqual(coordinates.cartesianToPostion(30, 0), 15)
		self.assertEqual(coordinates.cartesianToPostion(30, 1), 14)
		self.assertEqual(coordinates.cartesianToPostion(30, 2), 13)
		self.assertEqual(coordinates.cartesianToPostion(30, 7), 8)

		self.assertEqual(coordinates.cartesianToPostion(29, 0), 16)
		self.assertEqual(coordinates.cartesianToPostion(29, 1), 17)
		self.assertEqual(coordinates.cartesianToPostion(29, 2), 18)
		self.assertEqual(coordinates.cartesianToPostion(29, 7), 23)
  
		self.assertEqual(coordinates.cartesianToPostion(2, 0), 239)
		self.assertEqual(coordinates.cartesianToPostion(2, 1), 238)
		self.assertEqual(coordinates.cartesianToPostion(2, 2), 237)
		self.assertEqual(coordinates.cartesianToPostion(2, 7), 232)

		self.assertEqual(coordinates.cartesianToPostion(1, 0), 240)
		self.assertEqual(coordinates.cartesianToPostion(1, 1), 241)
		self.assertEqual(coordinates.cartesianToPostion(1, 2), 242)
		self.assertEqual(coordinates.cartesianToPostion(1, 7), 247)

		self.assertEqual(coordinates.cartesianToPostion(0, 0), 255)
		self.assertEqual(coordinates.cartesianToPostion(0, 1), 254)
		self.assertEqual(coordinates.cartesianToPostion(0, 2), 253)
		self.assertEqual(coordinates.cartesianToPostion(0, 7), 248)
  
if __name__ == '__main__':  # type: ignore
	unittest.main()