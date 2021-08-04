from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class GeoShape(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, address=None, addressCountry=None, box=None, circle=None, elevation=None, line=None, polygon=None, postalCode=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.address = address
        self.addressCountry = addressCountry
        self.box = box
        self.circle = circle
        self.elevation = elevation
        self.line = line
        self.polygon = polygon
        self.postalCode = postalCode

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_addressCountry(self, addressCountry):
        self.addressCountry = addressCountry

    def get_addressCountry(self):
        return self.addressCountry

    def set_box(self, box):
        self.box = box

    def get_box(self):
        return self.box

    def set_circle(self, circle):
        self.circle = circle

    def get_circle(self):
        return self.circle

    def set_elevation(self, elevation):
        self.elevation = elevation

    def get_elevation(self):
        return self.elevation

    def set_line(self, line):
        self.line = line

    def get_line(self):
        return self.line

    def set_polygon(self, polygon):
        self.polygon = polygon

    def get_polygon(self):
        return self.polygon

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
