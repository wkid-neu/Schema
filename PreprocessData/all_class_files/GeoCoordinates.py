from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class GeoCoordinates(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, address=None, addressCountry=None, elevation=None, latitude=None, longitude=None, postalCode=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.address = address
        self.addressCountry = addressCountry
        self.elevation = elevation
        self.latitude = latitude
        self.longitude = longitude
        self.postalCode = postalCode

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_addressCountry(self, addressCountry):
        self.addressCountry = addressCountry

    def get_addressCountry(self):
        return self.addressCountry

    def set_elevation(self, elevation):
        self.elevation = elevation

    def get_elevation(self):
        return self.elevation

    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_latitude(self):
        return self.latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_longitude(self):
        return self.longitude

    def set_postalCode(self, postalCode):
        self.postalCode = postalCode

    def get_postalCode(self):
        return self.postalCode


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
