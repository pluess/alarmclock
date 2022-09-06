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
# neodraw.line(0,0,0,7, green)
# neodraw.line(31,0,31,7, green)

# neodraw.line(1,1,1,6, blue)
# neodraw.line(30,1,30,6, blue)

i = -32

while (True):
	neodraw.letter(i, 0, '1', green)
	neodraw.letter(i+8, 0, '2', green)
	neodraw.letter(i+16, 0, '3', green)
	neodraw.letter(i+24, 0, '4', green)
	neodraw.letter(i+32, 0, '1', green)
	neodraw.letter(i+40, 0, '2', green)
	neodraw.letter(i+48, 0, '3', green)
	neodraw.letter(i+56, 0, '4', green)
	time.sleep(0.2)
	i += 1
	if i==0:
		i=-32

pixels.show()
