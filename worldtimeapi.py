import json
from logutil import get_logger

url = 'https://worldtimeapi.org/api/timezone/'
timeZoneZuerich = 'Europe/Zurich'

class WorldTimeApi:

    def __init__(self, httpgetter) -> None:
        self.httpgetter = httpgetter
        self.logger = get_logger(__name__)

    def getInternetTime(self):
        """
        Returns the current time from the internet.
        Sometimes we get an empty string instead of a JSON response. If
        this happens, we just try again (max 10 times).

        Returns:
            Tuple: (year, month, dayOfMonth, weekday, hour, minute, second, 0)
        """
        counter = 10
        while True:
            try:
                counter -= 1
                jsonTime = self.httpgetter.get_body(self.httpgetter.http_get(url+timeZoneZuerich))
                self.logger.info(jsonTime)
                currentTime = self._parseDateTime(jsonTime)
                return currentTime
            except ValueError as e:
                if counter > 0:
                    pass
                else:
                    self.logger.exception("Max retry count reached.")
                    raise e
                    

    def _parseDateTime(self, dateTimeJsonString : str):
        """_summary_

        Args:
            dateTimeJsonString (str): E.g. {"abbreviation":"CEST","client_ip":"178.192.81.185","datetime":"2022-09-07T16:12:43.772110+02:00","day_of_week":3,"day_of_year":250,"dst":true,"dst_from":"2022-03-27T01:00:00+00:00","dst_offset":3600,"dst_until":"2022-10-30T01:00:00+00:00","raw_offset":3600,"timezone":"Europe/Zurich","unixtime":1662559963,"utc_datetime":"2022-09-07T14:12:43.772110+00:00","utc_offset":"+02:00","week_number":36}
        """

        dateTimeJson = json.loads(dateTimeJsonString)
        dateTimeStr = dateTimeJson['datetime']

        # 2022-09-07T15:27:19.977367+02:00
        # 0    5  8  1  1  1  2      2  3  
        #            1  4  7  0      7  0
        year = int(dateTimeStr[0:4])
        month = int(dateTimeStr[5:7])
        dayOfMonth = int(dateTimeStr[8:10])
        hour = int(dateTimeStr[11:13])
        minute = int(dateTimeStr[14:16])
        second = int(dateTimeStr[17:19])
        weekday = dateTimeJson['day_of_week']

        return (year, month, dayOfMonth, weekday, hour, minute, second, 0)