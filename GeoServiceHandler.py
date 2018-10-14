from http.server import BaseHTTPRequestHandler
import json
from GeoDataClasses import GeoResponse
from urllib.parse import parse_qs
import Utils
from GeoServices.GoogleGeoService import GoogleGeoService
from GeoServices.BingGeoService import BingGeoService


class GeoServiceHandler(BaseHTTPRequestHandler):

    _geocode_path = '/geolocation?'
    _address_param = 'address'

    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'json')
        self.end_headers()

        while True:
            if not str.startswith(self.path, GeoServiceHandler._geocode_path):
                json_response = GeoServiceHandler._create_invalid_path_json()
                break

            params = parse_qs(self.path[len(GeoServiceHandler._geocode_path):])
            if GeoServiceHandler._address_param not in params:
                json_response = GeoServiceHandler._create_invalid_address_json()
                break

            json_response = GeoServiceHandler._get_geo_location(params[GeoServiceHandler._address_param])
            break

        self.wfile.write(json_response)

    @staticmethod
    def _get_geo_location(address):

        # the services will be processed in the order of the list
        services = [{'name': 'google', 'class': GoogleGeoService},
                    {'name': 'bing', 'class': BingGeoService}]
        keys = Utils.get_api_keys()

        for service in services:
            key = keys.get(service['name'])
            print("_get_geo_location: Service {0} geotranslation check started..".format(service['name']))
            if key:
                geo_service = service['class'](key)
                geo_coordinate = geo_service.get_geocordinate(address)
                if geo_coordinate:
                    print(geo_coordinate)
                    result = GeoServiceHandler._create_success_json(geo_coordinate, service['name'])
                    return result
            print("_get_geo_location: Service {0} has failed..".format(service['name']))

        result = GeoServiceHandler._create_service_failure_json()
        return result


    @staticmethod
    def _create_success_json(geo_coordinate, service):
        result = GeoResponse(
            status='OK',
            description='Geo location retrieved successfully',
            payload=geo_coordinate.__dict__,
            geoservice=service)
        return json.dumps(result.__dict__).encode('utf-8')

    @staticmethod
    def _create_invalid_address_json():
        result = GeoResponse(
            status='Invalid address',
            description= 'Address parameter missing in the request sent.',
            payload=None,
            geoservice=None)
        return json.dumps(result.__dict__).encode('utf-8')

    @staticmethod
    def _create_invalid_path_json():
        result = GeoResponse(
            status= 'Invalid request',
            description='Please use <url>:<port>/geocordinate?address:<address string> template for the request',
            payload =None,
            geoservice =None)
        return json.dumps(result.__dict__).encode('utf-8')

    @staticmethod
    def _create_service_failure_json():
        result = GeoResponse(
            status='Service failure',
            description='Service unavailable at the moment',
            payload=None,
            geoservice=None)
        return json.dumps(result.__dict__).encode('utf-8')

