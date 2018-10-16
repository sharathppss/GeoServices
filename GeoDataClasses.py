from dataclasses import dataclass


@dataclass
class GeoCoordinate:

    latitude: str
    longitude: str


@dataclass
class GeoResponse:
    """
    status: supports values OK|Invalid address|Invalid request|Service failure
    description: contains description of status
    geoservice: geoservice used to geocoordinate if successful else None
    payload: has geocoordinate object if successful else None
    """
    status: str
    description: str
    geoservice: str
    payload: GeoCoordinate



