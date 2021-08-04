from PreprocessData.all_class_files.Audience import Audience
import global_data


class EducationalAudience(Audience):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, audienceType=None, geographicArea=None, educationalRole=None):
        Audience.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, audienceType, geographicArea)
        self.educationalRole = educationalRole

    def set_educationalRole(self, educationalRole):
        self.educationalRole = educationalRole

    def get_educationalRole(self):
        return self.educationalRole


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
