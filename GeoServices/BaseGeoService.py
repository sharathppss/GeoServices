from abc import abstractmethod


class BaseGeoService:

    @abstractmethod
    def get_geocordinate(self, address):
        pass