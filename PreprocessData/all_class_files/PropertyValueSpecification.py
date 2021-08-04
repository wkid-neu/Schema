from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class PropertyValueSpecification(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, defaultValue=None, maxValue=None, minValue=None, multipleValues=None, readonlyValue=None, stepValue=None, valueMaxLength=None, valueMinLength=None, valueName=None, valuePattern=None, valueRequired=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.defaultValue = defaultValue
        self.maxValue = maxValue
        self.minValue = minValue
        self.multipleValues = multipleValues
        self.readonlyValue = readonlyValue
        self.stepValue = stepValue
        self.valueMaxLength = valueMaxLength
        self.valueMinLength = valueMinLength
        self.valueName = valueName
        self.valuePattern = valuePattern
        self.valueRequired = valueRequired

    def set_defaultValue(self, defaultValue):
        self.defaultValue = defaultValue

    def get_defaultValue(self):
        return self.defaultValue

    def set_maxValue(self, maxValue):
        self.maxValue = maxValue

    def get_maxValue(self):
        return self.maxValue

    def set_minValue(self, minValue):
        self.minValue = minValue

    def get_minValue(self):
        return self.minValue

    def set_multipleValues(self, multipleValues):
        self.multipleValues = multipleValues

    def get_multipleValues(self):
        return self.multipleValues

    def set_readonlyValue(self, readonlyValue):
        self.readonlyValue = readonlyValue

    def get_readonlyValue(self):
        return self.readonlyValue

    def set_stepValue(self, stepValue):
        self.stepValue = stepValue

    def get_stepValue(self):
        return self.stepValue

    def set_valueMaxLength(self, valueMaxLength):
        self.valueMaxLength = valueMaxLength

    def get_valueMaxLength(self):
        return self.valueMaxLength

    def set_valueMinLength(self, valueMinLength):
        self.valueMinLength = valueMinLength

    def get_valueMinLength(self):
        return self.valueMinLength

    def set_valueName(self, valueName):
        self.valueName = valueName

    def get_valueName(self):
        return self.valueName

    def set_valuePattern(self, valuePattern):
        self.valuePattern = valuePattern

    def get_valuePattern(self):
        return self.valuePattern

    def set_valueRequired(self, valueRequired):
        self.valueRequired = valueRequired

    def get_valueRequired(self):
        return self.valueRequired


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
