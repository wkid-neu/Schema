from PreprocessData.all_class_files.Audience import Audience
import global_data


class BusinessAudience(Audience):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, audienceType=None, geographicArea=None, numberOfEmployees=None, yearlyRevenue=None, yearsInOperation=None):
        Audience.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, audienceType, geographicArea)
        self.numberOfEmployees = numberOfEmployees
        self.yearlyRevenue = yearlyRevenue
        self.yearsInOperation = yearsInOperation

    def set_numberOfEmployees(self, numberOfEmployees):
        self.numberOfEmployees = numberOfEmployees

    def get_numberOfEmployees(self):
        return self.numberOfEmployees

    def set_yearlyRevenue(self, yearlyRevenue):
        self.yearlyRevenue = yearlyRevenue

    def get_yearlyRevenue(self):
        return self.yearlyRevenue

    def set_yearsInOperation(self, yearsInOperation):
        self.yearsInOperation = yearsInOperation

    def get_yearsInOperation(self):
        return self.yearsInOperation


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
