from GeoDataClasses import GeoCoordinate
from urllib.parse import urlencode
import Utils


class BingGeoService:

    _bing_url = "https://dev.virtualearth.net/REST/v1/Locations"

    def __init__(self, api_key):
        self.base_url = BingGeoService._bing_url
        self.key = api_key

    def _create_url(self, address):
        """

        :param address:
        :return: url string with params
        """

        url_params = dict()
        url_params["q"] = address
        url_params["key"] = self.key
        url_params["o"] = "json"
        url = self.base_url + "?" + urlencode(url_params)
        return url

    def get_geocordinate(self, address):
        """

        :param address: string address to be translated to coordinate
        :return: GeoCoordinate object if successful else None
        """

        url = self._create_url(address)
        response = Utils.make_webcall(url)
        if response is None:
            print("get_geocordinate: call to retrieve geolocation failed")
            return None

        return BingGeoService._translate_response(response)

    @staticmethod
    def _translate_response(response):
        """ Extract geocoordinate information from json returned from webcall.

        :param response: json string from webcall.
        :return: GeoCoordinate object if success else None
        """

        try:
            if response['statusCode'] == 200:
                location = response['resourceSets'][0]['resources'][0]['point']
                result = GeoCoordinate(location["coordinates"][0], location["coordinates"][1])
                return result

            else:
                print('_translate_response: Invalid response received, status: {0}'.format(response['status']))
                return None

        except Exception as error:
            print("_translate_response: Exception parsing the result: {0}".format(error))
            return None
