from pi_pico_neopixel.neopixel import Neopixel
from neodraw import NeoDraw
from coordinates import Cooridnates
from numbers6x8 import Numbers6x8
import time
 
numpix = 256
pixels = Neopixel(numpix, 0, 28, "GRB")
coordinates = Cooridnates(numpix, 8, True)
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
 
pixels.brightness(5)
pixels.clear()

neodraw = NeoDraw(pixels, coordinates, Numbers6x8(), True)

neodraw.letter(0, 0, '1', green)
neodraw.letter(6, 0, '2', green)
neodraw.letter(12, 0, 'colon', green)
neodraw.letter(18, 0, '3', green)
neodraw.letter(24, 0, '4', green)
pixels.show()
