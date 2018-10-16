from GeoDataClasses import GeoCoordinate
from urllib.parse import urlencode
import Utils


class GoogleGeoService:

    _google_url = "https://maps.googleapis.com/maps/api/geocode/json"

    def __init__(self, api_key):
        self.base_url = GoogleGeoService._google_url
        self.key = api_key

    def _create_url(self, address):
        """

        :param address:
        :return: url string with params
        """

        url_params = dict()
        url_params["address"] = address
        url_params["key"] = self.key
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

        return GoogleGeoService._translate_response(response)

    @staticmethod
    def _translate_response(response):
        """ Extract geocoordinate information from json returned from webcall.

        :param response: json string from webcall.
        :return: GeoCoordinate object if success else None
        """

        try:
            if response['status'] == 'OK':
                location = response['results'][0]['geometry']['location']
                result = GeoCoordinate(location['lat'], location['lng'] )
                return result

            else:
                print('_translate_response: Invalid response received, status: {0}'.format(response['status']))
                return None

        except Exception as error:
            print("_translate_response: Exception parsing the result: {0}".format(error))
            return None
