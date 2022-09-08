from neodraw import NeoDraw

class Display:

    def __init__(self, time, neodraw : NeoDraw, isLogging : bool = False) -> None:
        
        yellow = (255, 100, 0)
        orange = (255, 50, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        red = (255, 0, 0)
        self.color = blue
        
        self.neodraw = neodraw
        self.time = time
        self.isLogging = isLogging

    def getTimeStrings(self):
        currentTime = self.time.localtime()
        hour = currentTime[3]
        minute = currentTime[4]
        hourString = '{:02d}'.format(hour)
        minuteString = '{:02d}'.format(minute)
        return (hourString, minuteString)

    def showTime(self):
        hours, minutes = self.getTimeStrings()
        if self.isLogging is True: print('{}:{}'.format(hours, minutes))
        self.neodraw.clear()
        self.neodraw.letter(0,0,hours[0], self.color)
        self.neodraw.letter(6,0,hours[1], self.color)
        self.neodraw.letter(12,0,'colon', self.color)
        self.neodraw.letter(18,0,minutes[0], self.color)
        self.neodraw.letter(24,0,minutes[1], self.color)
        self.neodraw.show()
        