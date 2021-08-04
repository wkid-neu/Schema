from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class TypeAndQuantityNode(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, amountOfThisGood=None, businessFunction=None, typeOfGood=None, unitCode=None, unitText=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.amountOfThisGood = amountOfThisGood
        self.businessFunction = businessFunction
        self.typeOfGood = typeOfGood
        self.unitCode = unitCode
        self.unitText = unitText

    def set_amountOfThisGood(self, amountOfThisGood):
        self.amountOfThisGood = amountOfThisGood

    def get_amountOfThisGood(self):
        return self.amountOfThisGood

    def set_businessFunction(self, businessFunction):
        self.businessFunction = businessFunction

    def get_businessFunction(self):
        return self.businessFunction

    def set_typeOfGood(self, typeOfGood):
        self.typeOfGood = typeOfGood

    def get_typeOfGood(self):
        return self.typeOfGood

    def set_unitCode(self, unitCode):
        self.unitCode = unitCode

    def get_unitCode(self):
        return self.unitCode

    def set_unitText(self, unitText):
        self.unitText = unitText

    def get_unitText(self):
        return self.unitText


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
