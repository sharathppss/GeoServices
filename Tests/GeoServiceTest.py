import unittest
from GeoServices.GoogleGeoService import GoogleGeoService
from GeoServices.BingGeoService import BingGeoService
import Utils
import ssl


class GoogleGeoServiceTests(unittest.TestCase):

    def test_happy_flow(self):

        api_keys = Utils.get_api_keys()
        address = '3530 Hughes Avenue, Los Angeles 90034'
        service = GoogleGeoService(api_keys['google'])
        coordinate = service.get_geocordinate(address)
        print(coordinate)
        self.assertEqual(coordinate.latitude, 34.0285467)
        self.assertEqual(coordinate.longitude, -118.4023899)


class BingGeoServiceTests(unittest.TestCase):

    def test_happy_flow(self):

        api_keys = Utils.get_api_keys()
        address = '3530 Hughes Avenue, Los Angeles 90034'
        service = BingGeoService(api_keys['bing'])
        coordinate = service.get_geocordinate(address)
        print(coordinate)
        self.assertEqual(coordinate.latitude, 34.02851)
        self.assertEqual(coordinate.longitude, -118.40239)


if __name__ == '__main__':

    unittest.main()
