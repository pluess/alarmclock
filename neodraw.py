from coordinates import Cooridnates
from coordinates import PositionOutOfRangeError
from c64german import C64German

class NeoDraw:

	def __init__(self, neopixel, coordiantes : Cooridnates, c64german:C64German = None) -> None:  # type: ignore
		self.neopixel = neopixel
		self.coordiantes = coordiantes
		self.c64german = c64german

	def line(self, x1 : int, y1 : int, x2 : int, y2 : int, rgb) -> None:
		deltaX = x2-x1
		deltaY = y2-y1
		delta = max(abs(deltaX), abs(deltaY))
		stepX = deltaX / delta
		stepY = deltaY / delta

		x = x1
		y = y1
		self.neopixel.set_pixel(self.coordiantes.cartesianToPostion(x, y), rgb)
		for i in range(0, delta):
			x += stepX
			y += stepY
			self.neopixel.set_pixel(self.coordiantes.cartesianToPostion(int(x), int(y)), rgb)

	def letter(self, x : int, y : int, letter :str, rgb):
		if (self.c64german==None):
			raise BaseException('c64german font not defined')
		topDownBitMapList = self.c64german[letter]
		bottomUpBitMapList = topDownBitMapList[::-1] # reverse
		for bitMapRow in range(0, len(bottomUpBitMapList)):  # type: ignore
			binaryString = self.c64german.toBinaryString(bottomUpBitMapList[bitMapRow])  # type: ignore
			for bitPosition in range(0, len(binaryString)):
				if (binaryString[bitPosition]=='1'):
					try:
						xPos = x + bitPosition
						yPos = y + bitMapRow
						self.neopixel.set_pixel(self.coordiantes.cartesianToPostion(xPos, yPos), rgb)
					except PositionOutOfRangeError:
						pass