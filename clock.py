from machine import RTC
from machine import Timer
import time
import secrets
from wlanconnector import WlanConnector
import network
from worldtimeapi import WorldTimeApi
from display import Display
from pi_pico_neopixel.neopixel import Neopixel
from neodraw import NeoDraw
from coordinates import Cooridnates
from numbers6x8 import Numbers6x8
import httpgetter

def setRTC():
    WlanConnector(network).connect(secrets.ssid, secrets.password)  # type: ignore
    worldTimeApi = WorldTimeApi(httpgetter)
    RTC().datetime(worldTimeApi.getInternetTime())
    print(RTC().datetime())

setRTC()

numpix = 256
neopixels = Neopixel(numpix, 0, 28, "GRB")
coordinates = Cooridnates(numpix, 8)
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
 
neopixels.brightness(5)
neopixels.clear()

neodraw = NeoDraw(neopixels, coordinates, Numbers6x8())

display = Display(time, neodraw, True)
display.showTime()


t1 = Timer(period=60000, mode=Timer.PERIODIC, callback=lambda t:display.showTime())
t2 = Timer(period=15*60000, mode=Timer.PERIODIC, callback=lambda t:setRTC())
    

