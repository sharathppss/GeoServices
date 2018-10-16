GeoService Proxy Service

A REST HTTP-GET Interface based GeoService that translates address to co-ordinates for the caller.
The proxy service is based on multiple web geo services with service calls made in the specific order until valid
response is recieved. Currently google and bing services supported (in that order).

Request URL template:

    <ip address>:<port>/geolocation?address:<address string> template

JSON Response values:

    status: status of request  - OK|Invalid address|Invalid request|Service failure
    description: contains description of status
    geoservice: geoservice used to get geocoordinate if "OK" status else None
    payload: geocoordinate json (latitude and longitude) if "OK" status else None

Sample Request:

 http://localhost:4444/geolocation?address=%223530%20Hughes%20Avenue%22

Sample Response:

{
    "status": "OK",
    "description": "Geo location retrieved successfully",
    "geoservice": "google",
    "payload":
    {
        "latitude": 34.0285467,
        "longitude": -118.4023899
    }
}

Requirements:

+ Python 3.7
+ ApiKeys.txt (not present on repository)

Usage:

+ Get ApiKeys.txt file and place at root of project.
+ Move to the root folder and start the server with below command:
    example: python RunServer.py --ipadd 127.0.0.1 --port 5555
+ Make get request as indicated above.

