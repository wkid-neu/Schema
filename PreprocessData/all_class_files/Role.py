from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Role(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, endDate=None, roleName=None, startDate=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.endDate = endDate
        self.roleName = roleName
        self.startDate = startDate

    def set_endDate(self, endDate):
        self.endDate = endDate

    def get_endDate(self):
        return self.endDate

    def set_roleName(self, roleName):
        self.roleName = roleName

    def get_roleName(self):
        return self.roleName

    def set_startDate(self, startDate):
        self.startDate = startDate

    def get_startDate(self):
        return self.startDate


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
