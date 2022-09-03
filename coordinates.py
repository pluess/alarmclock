class Cooridnates:

	def __init__(self, numberOfLeds : int, matrixHeight : int) -> None:
		self.numberOfLeds = numberOfLeds
		self.maxPosition = numberOfLeds - 1
		self.matrixHeight = matrixHeight
		self.yOffset = matrixHeight -1
		self.moduloRemainder = (numberOfLeds // matrixHeight) % 2

	def cartesianToPostion(self, x : int, y : int) -> int:
		if (x % 2 == self.moduloRemainder):
			return self.maxPosition - self.matrixHeight*x - y
		else:
			return self.maxPosition - self.matrixHeight*x -self.yOffset + y
