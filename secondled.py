from pi_pico_neopixel.neopixel import Neopixel
from neodraw import NeoDraw
from coordinates import Cooridnates
 
numpix = 256
pixels = Neopixel(numpix, 0, 28, "GRB")
coordinates = Cooridnates(numpix, 8)
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
 
pixels.brightness(5)
pixels.clear()

neodraw = NeoDraw(pixels, coordinates)
neodraw.line(0,0,31,0, red)
neodraw.line(0,7,31,7, red)
neodraw.line(0,0,0,7, red)
neodraw.line(31,0,31,7, red)

neodraw.line(1,1,30,1, blue)
neodraw.line(1,6,30,6, blue)
neodraw.line(1,1,1,6, blue)
neodraw.line(30,1,30,6, blue)

# neodraw.line(0,0,7,7, green)
# neodraw.line(0,7,7,0, green)

# neodraw.line(24,7,31,0, green)
# neodraw.line(24,0,31,7, green)

neodraw.line(2,2,29,5, green)
neodraw.line(2,5,29,2, green)

pixels.show()
