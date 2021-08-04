from PreprocessData.all_class_files.PropertyValue import PropertyValue
import global_data


class LocationFeatureSpecification(PropertyValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, maxValue=None, minValue=None, propertyID=None, unitCode=None, unitText=None, value=None, valueReference=None, hoursAvailable=None, validFrom=None, validThrough=None):
        PropertyValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, maxValue, minValue, propertyID, unitCode, unitText, value, valueReference)
        self.hoursAvailable = hoursAvailable
        self.validFrom = validFrom
        self.validThrough = validThrough

    def set_hoursAvailable(self, hoursAvailable):
        self.hoursAvailable = hoursAvailable

    def get_hoursAvailable(self):
        return self.hoursAvailable

    def set_validFrom(self, validFrom):
        self.validFrom = validFrom

    def get_validFrom(self):
        return self.validFrom

    def set_validThrough(self, validThrough):
        self.validThrough = validThrough

    def get_validThrough(self):
        return self.validThrough


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
