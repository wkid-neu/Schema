from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class OwnershipInfo(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, acquiredFrom=None, ownedFrom=None, ownedThrough=None, typeOfGood=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.acquiredFrom = acquiredFrom
        self.ownedFrom = ownedFrom
        self.ownedThrough = ownedThrough
        self.typeOfGood = typeOfGood

    def set_acquiredFrom(self, acquiredFrom):
        self.acquiredFrom = acquiredFrom

    def get_acquiredFrom(self):
        return self.acquiredFrom

    def set_ownedFrom(self, ownedFrom):
        self.ownedFrom = ownedFrom

    def get_ownedFrom(self):
        return self.ownedFrom

    def set_ownedThrough(self, ownedThrough):
        self.ownedThrough = ownedThrough

    def get_ownedThrough(self):
        return self.ownedThrough

    def set_typeOfGood(self, typeOfGood):
        self.typeOfGood = typeOfGood

    def get_typeOfGood(self):
        return self.typeOfGood


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
