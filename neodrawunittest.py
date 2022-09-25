import application 

import unittest
from coordinates import Cooridnates
from neodraw import NeoDraw
from font import Font

class NeopixelMock:

	def __init__(self, num_leds, state_machine, pin, mode="RGB", delay=0.0001):
		self.num_leds = num_leds
		self.drawnPixel = {}
		pass

	def set_pixel(self, pixel_num, rgb_w, how_bright=None):
		assert isinstance(pixel_num, int), "int expected, given="+str(pixel_num)
		assert self.num_leds > pixel_num, "pixel_num="+str(pixel_num)+" is bigger than self.num_leds="+str(self.num_leds)
		assert 0 <= pixel_num, "pixel_num="+str(pixel_num)+" is smaller than 0" 
		if rgb_w in self.drawnPixel:
			self.drawnPixel[rgb_w].append(pixel_num)
		else:
			self.drawnPixel[rgb_w] = [pixel_num]

class FontMock1(Font):

	def __init__(self) -> None:
		self.width = 4
		self.height = 4
		pass

	def __getitem__(self, key) -> list:  # type: ignore
		if (key=='A'):
			return [0b1010,0b0101,0b1111,0b0000]
		else:
			raise NotImplementedError(key)

class FontMock2(Font):

	def __init__(self) -> None:
		self.width = 4
		self.height = 4
		pass

	def __getitem__(self, key) -> list:  # type: ignore
		if (key=='A'):
			return [0b0000,0b1111,0b1111,0b0000]
		else:
			raise NotImplementedError(key)

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
		self.neopixel =  NeopixelMock(numpix, 0, 28, "GRB")
		self.coordinates = Cooridnates(numpix, 4)
		self.neodraw = NeoDraw(self.neopixel, self.coordinates, FontMock1())
		self.red = (255,0,0)
		self.black = (0,0,0)

	def test_line_cross_right(self):
		self.neodraw.line(0, 0, 3, 3, self.red)
		self.assertEqual(self.neopixel.drawnPixel[self.red], [15, 9 , 5, 3])

	def test_line_crossl_left(self):
		self.neodraw.line(0, 3, 3, 0, self.red)
		self.assertEqual(self.neopixel.drawnPixel[self.red], [12, 10, 6, 0])

	def test_line_bottom(self):
		self.neodraw.line(0, 0, 3, 0, self.red)
		self.assertEqual(self.neopixel.drawnPixel[self.red], [15, 8 , 7, 0])

	def test_letter_no_font(self):
		neodraw = NeoDraw(self.neopixel, self.coordinates)
		try:
			neodraw.letter(0, 0, 'B', (255, 0, 0))
			self.fail('BaseException expected, because no font is set.')
		except BaseException:
			pass

	def test_letter(self):
		self.neodraw.letter(0, 0, 'A', self.red)
		self.assertEqual(self.neopixel.drawnPixel[self.red], [14, 9, 6, 1, 10, 2, 12, 4])
		self.assertEqual(self.neopixel.drawnPixel[self.black], [15, 8, 7, 0, 13, 5, 11, 3])

	def test_letter_different_font(self):
		self.neodraw.letter(0, 0, 'A', self.red, FontMock2())
		self.assertEqual(self.neopixel.drawnPixel[self.red], [14, 9, 6, 1, 13, 10, 5, 2]	)
		self.assertEqual(self.neopixel.drawnPixel[self.black], [15, 8, 7, 0, 12, 11, 4, 3])

	def test_letter_shiftedWithClipping(self):
		self.neodraw.letter(1, 1, 'A', (255, 0, 0))
		self.assertEqual(self.neopixel.drawnPixel[self.red], [10, 5, 2, 4])
		self.assertEqual(self.neopixel.drawnPixel[self.black], [9, 6, 1, 11, 3])

if __name__ == '__main__':  # type: ignore
	unittest.main()