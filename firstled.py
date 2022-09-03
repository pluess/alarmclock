import time
from pi_pico_neopixel.neopixel import Neopixel
 
numpix = 256
pixels = Neopixel(numpix, 0, 28, "GRB")
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
 
pixels.brightness(5)
pixels.fill(orange)
pixels.set_pixel_line_gradient(0, numpix-1, red, blue)
pixels.show()
while True:
	time.sleep(0.01)
	pixels.rotate_right(1)
	pixels.show()

