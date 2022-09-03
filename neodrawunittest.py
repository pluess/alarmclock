import unittest
from coordinates import Cooridnates
from neodraw import NeoDraw

class Neopixel:

	def __init__(self, num_leds, state_machine, pin, mode="RGB", delay=0.0001):
		self.num_leds = num_leds
		self.drawnPixel = []
		pass

	def set_pixel(self, pixel_num, rgb_w, how_bright=None):
		assert isinstance(pixel_num, int), "int expected, given="+str(pixel_num)
		assert self.num_leds > pixel_num, "pixel_num="+str(pixel_num)+" is bigger than self.num_leds="+str(self.num_leds)
		assert 0 <= pixel_num, "pixel_num="+str(pixel_num)+" is smaller than 0" 
		self.drawnPixel.append(pixel_num)
		pass

"""
4x4
===
12 ---- 11  04 ---- 03
13 !  ! 10  05 !  ! 02
14 !  ! 09  06 !  ! 01 
15 !  ! 08  07 !  ! 00
      ----------
"""
class NeoDrawUnitTest(unittest.TestCase):

	def setUp(self):

		numpix = 16
		self.neopixel =  Neopixel(numpix, 0, 28, "GRB")
		self.coordinates = Cooridnates(numpix, 4)
		self.neodraw = NeoDraw(self.neopixel, self.coordinates)	  # type: ignore

	def test_line_cross_right(self):
		self.neodraw.line(0, 0, 3, 3, (255, 0 ,0))
		self.assertEqual(self.neopixel.drawnPixel, [15, 9 , 5, 3])

	def test_line_crossl_left(self):
		self.neodraw.line(0, 3, 3, 0, (255, 0 ,0))
		self.assertEqual(self.neopixel.drawnPixel, [12, 10, 6, 0])

	def test_line_bottom(self):
		self.neodraw.line(0, 0, 3, 0, (255, 0 ,0))
		self.assertEqual(self.neopixel.drawnPixel, [15, 8 , 7, 0])

if __name__ == '__main__':  # type: ignore
	unittest.main()