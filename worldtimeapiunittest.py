import re
import unittest
from worldtimeapi import WorldTimeApi
import httpgetter

class HttpGetterMock:

    def __init__(self, failedReds : int = 0) -> None:
        self.failedReds = failedReds
        with open('response.log','rb') as rf:
            self.mockResponse = rf.read()
            self.mockResponse = self.mockResponse.decode('utf-8')

    def http_get(self, url):
        if self.failedReds > 0:
            self.failedReds -= 1
            return ""
        else:
            return self.mockResponse
    
    def get_body(self, response):
        return httpgetter.get_body(response)


class WorldTimeApiUnitTest(unittest.TestCase):


    def test__parseDateTime(self):
        worldTimeApi = WorldTimeApi(HttpGetterMock())
        testString = '{"abbreviation":"CEST","client_ip":"178.192.81.185","datetime":"2022-09-07T16:12:43.772110+02:00","day_of_week":3,"day_of_year":250,"dst":true,"dst_from":"2022-03-27T01:00:00+00:00","dst_offset":3600,"dst_until":"2022-10-30T01:00:00+00:00","raw_offset":3600,"timezone":"Europe/Zurich","unixtime":1662559963,"utc_datetime":"2022-09-07T14:12:43.772110+00:00","utc_offset":"+02:00","week_number":36}'
        actualDateTime = worldTimeApi._parseDateTime(testString)
        expectedDateTime=(2022, 9, 7, 3, 16, 12, 43, 0)
        self.assertEqual(actualDateTime, expectedDateTime)

    def test_getInternetTime(self):
        worldTimeApi = WorldTimeApi(HttpGetterMock())
        actualDateTime = worldTimeApi.getInternetTime()
        expectedDateTime = (2022, 9, 8, 4, 11, 15, 59, 0)
        self.assertEqual(actualDateTime, expectedDateTime)

    def test_getInternetTime_two_fails(self):
        worldTimeApi = WorldTimeApi(HttpGetterMock(2))
        actualDateTime = worldTimeApi.getInternetTime()
        expectedDateTime = (2022, 9, 8, 4, 11, 15, 59, 0)
        self.assertEqual(actualDateTime, expectedDateTime)

    def test_getInternetTime_complete_fail(self):
        try:
            worldTimeApi = WorldTimeApi(HttpGetterMock(11))
            actualDateTime = worldTimeApi.getInternetTime()
            self.fail('Expected ValueError')
        except ValueError:
            pass

if __name__ == '__main__':  # type: ignore
    unittest.main()