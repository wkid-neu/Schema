from PreprocessData.all_class_files.GeoShape import GeoShape
import global_data


class GeoCircle(GeoShape):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, address=None, addressCountry=None, box=None, circle=None, elevation=None, line=None, polygon=None, postalCode=None, geoMidpoint=None, geoRadius=None):
        GeoShape.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, address, addressCountry, box, circle, elevation, line, polygon, postalCode)
        self.geoMidpoint = geoMidpoint
        self.geoRadius = geoRadius

    def set_geoMidpoint(self, geoMidpoint):
        self.geoMidpoint = geoMidpoint

    def get_geoMidpoint(self):
        return self.geoMidpoint

    def set_geoRadius(self, geoRadius):
        self.geoRadius = geoRadius

    def get_geoRadius(self):
        return self.geoRadius


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
