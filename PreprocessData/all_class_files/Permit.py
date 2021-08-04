from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Permit(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, issuedBy=None, issuedThrough=None, permitAudience=None, validFor=None, validFrom=None, validIn=None, validUntil=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.issuedBy = issuedBy
        self.issuedThrough = issuedThrough
        self.permitAudience = permitAudience
        self.validFor = validFor
        self.validFrom = validFrom
        self.validIn = validIn
        self.validUntil = validUntil

    def set_issuedBy(self, issuedBy):
        self.issuedBy = issuedBy

    def get_issuedBy(self):
        return self.issuedBy

    def set_issuedThrough(self, issuedThrough):
        self.issuedThrough = issuedThrough

    def get_issuedThrough(self):
        return self.issuedThrough

    def set_permitAudience(self, permitAudience):
        self.permitAudience = permitAudience

    def get_permitAudience(self):
        return self.permitAudience

    def set_validFor(self, validFor):
        self.validFor = validFor

    def get_validFor(self):
        return self.validFor

    def set_validFrom(self, validFrom):
        self.validFrom = validFrom

    def get_validFrom(self):
        return self.validFrom

    def set_validIn(self, validIn):
        self.validIn = validIn

    def get_validIn(self):
        return self.validIn

    def set_validUntil(self, validUntil):
        self.validUntil = validUntil

    def get_validUntil(self):
        return self.validUntil


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
