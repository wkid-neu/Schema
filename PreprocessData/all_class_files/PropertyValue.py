from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class PropertyValue(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, maxValue=None, minValue=None, propertyID=None, unitCode=None, unitText=None, value=None, valueReference=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.maxValue = maxValue
        self.minValue = minValue
        self.propertyID = propertyID
        self.unitCode = unitCode
        self.unitText = unitText
        self.value = value
        self.valueReference = valueReference

    def set_maxValue(self, maxValue):
        self.maxValue = maxValue

    def get_maxValue(self):
        return self.maxValue

    def set_minValue(self, minValue):
        self.minValue = minValue

    def get_minValue(self):
        return self.minValue

    def set_propertyID(self, propertyID):
        self.propertyID = propertyID

    def get_propertyID(self):
        return self.propertyID

    def set_unitCode(self, unitCode):
        self.unitCode = unitCode

    def get_unitCode(self):
        return self.unitCode

    def set_unitText(self, unitText):
        self.unitText = unitText

    def get_unitText(self):
        return self.unitText

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_valueReference(self, valueReference):
        self.valueReference = valueReference

    def get_valueReference(self):
        return self.valueReference


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
