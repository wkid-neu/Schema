from PreprocessData.all_class_files.Enumeration import Enumeration
import global_data


class QualitativeValue(Enumeration):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalProperty=None, equal=None, greater=None, greaterOrEqual=None, lesser=None, lesserOrEqual=None, nonEqual=None, valueReference=None):
        Enumeration.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.additionalProperty = additionalProperty
        self.equal = equal
        self.greater = greater
        self.greaterOrEqual = greaterOrEqual
        self.lesser = lesser
        self.lesserOrEqual = lesserOrEqual
        self.nonEqual = nonEqual
        self.valueReference = valueReference

    def set_additionalProperty(self, additionalProperty):
        self.additionalProperty = additionalProperty

    def get_additionalProperty(self):
        return self.additionalProperty

    def set_equal(self, equal):
        self.equal = equal

    def get_equal(self):
        return self.equal

    def set_greater(self, greater):
        self.greater = greater

    def get_greater(self):
        return self.greater

    def set_greaterOrEqual(self, greaterOrEqual):
        self.greaterOrEqual = greaterOrEqual

    def get_greaterOrEqual(self):
        return self.greaterOrEqual

    def set_lesser(self, lesser):
        self.lesser = lesser

    def get_lesser(self):
        return self.lesser

    def set_lesserOrEqual(self, lesserOrEqual):
        self.lesserOrEqual = lesserOrEqual

    def get_lesserOrEqual(self):
        return self.lesserOrEqual

    def set_nonEqual(self, nonEqual):
        self.nonEqual = nonEqual

    def get_nonEqual(self):
        return self.nonEqual

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
