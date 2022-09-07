import secrets
from wlanconnector import WlanConnector
import network
import httpgetter
import worldtimeapi
from machine import RTC

def getTime():
    """
    Returns the current time from the internet.
    Sometimes we get an empty string instead of a JSON response. If
    this happens, we just try again (max 10 times).

    Returns:
        Tuple: (year, month, dayOfMonth, weekday, hour, minute, second, 0)
    """
    counter = 10
    while counter > 0:
        try:
            counter -= 1
            jsonTime = httpgetter.get_body(httpgetter.http_get(worldtimeapi.url+worldtimeapi.timeZoneZuerich))
            print(jsonTime)
            currentTime = worldtimeapi.parseDateTime(jsonTime)
            return currentTime
        except ValueError:
            pass

def setRTC():
    WlanConnector(network).connect(secrets.ssid, secrets.password)  # type: ignore
    RTC().datetime(getTime())
    print(RTC().datetime())

setRTC()
    

