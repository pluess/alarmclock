class Cooridnates:

	def __init__(self, numberOfLeds : int, matrixWidth : int) -> None:
		self.numberOfLeds = numberOfLeds
		self.maxPosition = numberOfLeds - 1
		self.matrixWidth = matrixWidth
		self.yOffset = matrixWidth -1

	def cartesianToPostion(self, x : int, y : int) -> int:
		if (x % 2 == 0):
			return self.maxPosition -self.matrixWidth*x - y
		else:
			return self.maxPosition - self.matrixWidth*x -self.yOffset + y
