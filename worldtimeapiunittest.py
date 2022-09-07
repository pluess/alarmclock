import unittest
import worldtimeapi

class WorldTimeApiUnitTest(unittest.TestCase):

    def test_no_connection(self):
        testString = '{"abbreviation":"CEST","client_ip":"178.192.81.185","datetime":"2022-09-07T16:12:43.772110+02:00","day_of_week":3,"day_of_year":250,"dst":true,"dst_from":"2022-03-27T01:00:00+00:00","dst_offset":3600,"dst_until":"2022-10-30T01:00:00+00:00","raw_offset":3600,"timezone":"Europe/Zurich","unixtime":1662559963,"utc_datetime":"2022-09-07T14:12:43.772110+00:00","utc_offset":"+02:00","week_number":36}'
        actualDateTime = worldtimeapi.parseDateTime(testString)
        expectedDateTime=(2022, 9, 7, 3, 16, 12, 43)
        self.assertEqual(actualDateTime, expectedDateTime)

if __name__ == '__main__':  # type: ignore
    unittest.main()