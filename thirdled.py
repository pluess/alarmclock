from pi_pico_neopixel.neopixel import Neopixel
from neodraw import NeoDraw
from coordinates import Cooridnates
from c64german import C64German
 
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

neodraw = NeoDraw(pixels, coordinates, C64German())
# neodraw.line(0,0,0,7, green)
# neodraw.line(31,0,31,7, green)

# neodraw.line(1,1,1,6, blue)
# neodraw.line(30,1,30,6, blue)

neodraw.letter(0, 0, '1', green)
neodraw.letter(7, 0, '2', green)
neodraw.letter(15, 0, '3', green)
neodraw.letter(23, 0, '4', green)

pixels.show()
