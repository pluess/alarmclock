from coordinates import Cooridnates

class NeoDraw:

	def __init__(self, neopixel, coordiantes : Cooridnates) -> None:
		self.neopixel = neopixel
		self.coordiantes = coordiantes

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


