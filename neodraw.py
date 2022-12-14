from coordinates import Cooridnates
from coordinates import PositionOutOfRangeError
from font import Font
from logutil import get_logger

class NeoDraw:

    def __init__(self, neopixel, coordiantes : Cooridnates, font:Font = None) -> None:  # type: ignore
        self.neopixel = neopixel
        self.coordiantes = coordiantes
        self.font = font
        self.logger = get_logger(__name__)

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
            self.logger.debug('x={0}, y={0}'.format(x,y))
            self.neopixel.set_pixel(self.coordiantes.cartesianToPostion(int(x), int(y)), rgb)

    def letter(self, x : int, y : int, letter :str, rgb, font: Font = None):  # type: ignore
        if font==None:
            localFont = self.font
        else:
            localFont = font
        if localFont==None:
            raise BaseException('font not defined')
        self.logger.debug('showing letter '+letter)
        topDownBitMapList = localFont[letter]
        bottomUpBitMapList = topDownBitMapList[::-1] # reverse
        for bitMapRow in range(0, len(bottomUpBitMapList)):
            binaryString = localFont.toBinaryString(bottomUpBitMapList[bitMapRow])
            self.logger.debug('{}: {}'.format(bitMapRow, binaryString))
            for bitPosition in range(0, len(binaryString)):
                if (binaryString[bitPosition]=='1'):
                    try:
                        xPos = x + bitPosition
                        yPos = y + bitMapRow
                        self.neopixel.set_pixel(self.coordiantes.cartesianToPostion(xPos, yPos), rgb)
                    except PositionOutOfRangeError:
                        pass
                else:
                    try:
                        xPos = x + bitPosition
                        yPos = y + bitMapRow
                        self.neopixel.set_pixel(self.coordiantes.cartesianToPostion(xPos, yPos), (0,0,0))
                    except PositionOutOfRangeError:
                        pass

    def clear(self):
        self.neopixel.clear()

    def show(self):
        self.neopixel.show()

