import urllib.request
import json
import ssl

APIKEYS_FILE = "ApiKeys"


def make_webcall(url):
    """ make webcall using url provided.

    :param url
    :return: json string if successful else None
    """
    try:
        request = urllib.request.Request(url)
        print(url)
        # TODO: find out about SSL certificate error
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        with urllib.request.urlopen(request, context=gcontext) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result

    except Exception as error:
        print("make_webcall: Exception making web call: {0}".format(error))
        return None


def get_api_keys():
    """ Load api_keys for all geoservices from a file at APIKEYS_FILE.

    :return: dict of keys if successful else Nonen
    """
    result = {}
    try:
        with open(APIKEYS_FILE, 'r', encoding='utf-8') as file:
            lines = file.read().splitlines()
        for line in lines:
            vals = line.split('=')
            result[vals[0]] = vals[1]

    except Exception as error:
        print("get_api_keys: Exception getting api keys: {0}".format(error))

    return result

