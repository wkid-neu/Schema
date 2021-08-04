from PreprocessData.all_class_files.Role import Role
import global_data


class OrganizationRole(Role):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, endDate=None, roleName=None, startDate=None, numberedPosition=None):
        Role.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, endDate, roleName, startDate)
        self.numberedPosition = numberedPosition

    def set_numberedPosition(self, numberedPosition):
        self.numberedPosition = numberedPosition

    def get_numberedPosition(self):
        return self.numberedPosition


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
