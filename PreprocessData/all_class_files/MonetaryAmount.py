from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class MonetaryAmount(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, currency=None, maxValue=None, minValue=None, validFrom=None, validThrough=None, value=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.currency = currency
        self.maxValue = maxValue
        self.minValue = minValue
        self.validFrom = validFrom
        self.validThrough = validThrough
        self.value = value

    def set_currency(self, currency):
        self.currency = currency

    def get_currency(self):
        return self.currency

    def set_maxValue(self, maxValue):
        self.maxValue = maxValue

    def get_maxValue(self):
        return self.maxValue

    def set_minValue(self, minValue):
        self.minValue = minValue

    def get_minValue(self):
        return self.minValue

    def set_validFrom(self, validFrom):
        self.validFrom = validFrom

    def get_validFrom(self):
        return self.validFrom

    def set_validThrough(self, validThrough):
        self.validThrough = validThrough

    def get_validThrough(self):
        return self.validThrough

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
