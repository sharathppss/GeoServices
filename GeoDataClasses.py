from dataclasses import dataclass


@dataclass
class GeoCoordinate:

    latitude: str
    longitude: str


@dataclass
class GeoResponse:

    status: str
    description: str
    geoservice: str
    payload: GeoCoordinate



