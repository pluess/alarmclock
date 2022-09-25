from logutil import get_logger

class PositionOutOfRangeError(Exception):

    def __init__(self,  x : int, y : int, maxX : int, maxY : int) -> None:
        self.x = x
        self.y = y
        self.maxX = maxX
        self.maxY = maxY

        super(PositionOutOfRangeError, self).__init__('x: {}, y: {} not in Range of 0-maxX: {}, 0-maxY: {}'.format(self.x, self.y, self.maxX, self.maxY))

class Cooridnates:

    def __init__(self, numberOfLeds : int, matrixHeight : int) -> None:
        self.numberOfLeds = numberOfLeds
        self.maxPosition = numberOfLeds - 1
        self.matrixHeight = matrixHeight
        self.yOffset = matrixHeight -1
        self.moduloRemainder = (numberOfLeds // matrixHeight) % 2
        self.maxX = self.numberOfLeds // matrixHeight - 1
        self.maxY = self.matrixHeight - 1
        self.logger = get_logger(__name__)

    def cartesianToPostion(self, x : int, y : int) -> int:
        if (x>self.maxX or y>self.maxY or x<0 or y<0):
            raise PositionOutOfRangeError(x, y, self.maxX, self.maxY)
        if (x % 2 == self.moduloRemainder):
            position = self.maxPosition - self.matrixHeight*x - y
        else:
            position = self.maxPosition - self.matrixHeight*x -self.yOffset + y
        self.logger.debug('position={0}'.format(position))
        return position
