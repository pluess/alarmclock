import application

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
from logutil import get_logger
import webrepl

logger = get_logger(__name__)

def setRTC():
    """
    Set RTC with current time from https://worldtimeapi.org/api/timezone/Europe/Zurich
    """
    worldTimeApi = WorldTimeApi(httpgetter)
    RTC().datetime(worldTimeApi.getInternetTime())
    logger.info(', '.join(str(x) for x in RTC().datetime()))

try:
    # connect to WLAN
    WlanConnector(network).connect(secrets.ssid, secrets.password)  # type: ignore
    # allow access via webrepl
    webrepl.start()

    setRTC()
    
    numpix = 256
    neopixels = Neopixel(numpix, 0, 28, "GRB")
    coordinates = Cooridnates(numpix, 8)
    
    neopixels.brightness(5)
    neopixels.clear()

    neodraw = NeoDraw(neopixels, coordinates, Numbers6x8())

    display = Display(time, neodraw)
    display.showTime()

    # update time very minute
    t1 = Timer(period=60000, mode=Timer.PERIODIC, callback=lambda t:display.showTime())
    # get current time every 15 minutes
    t2 = Timer(period=15*60000, mode=Timer.PERIODIC, callback=lambda t:setRTC())
    
except Exception as e:
    # just in case, log every exception
    logger.exc(e, 'Error in clock.')  # type: ignore
    raise e

