from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class OpeningHoursSpecification(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, closes=None, dayOfWeek=None, opens=None, validFrom=None, validThrough=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.closes = closes
        self.dayOfWeek = dayOfWeek
        self.opens = opens
        self.validFrom = validFrom
        self.validThrough = validThrough

    def set_closes(self, closes):
        self.closes = closes

    def get_closes(self):
        return self.closes

    def set_dayOfWeek(self, dayOfWeek):
        self.dayOfWeek = dayOfWeek

    def get_dayOfWeek(self):
        return self.dayOfWeek

    def set_opens(self, opens):
        self.opens = opens

    def get_opens(self):
        return self.opens

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
