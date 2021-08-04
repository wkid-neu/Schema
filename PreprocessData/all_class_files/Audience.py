from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Audience(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, audienceType=None, geographicArea=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.audienceType = audienceType
        self.geographicArea = geographicArea

    def set_audienceType(self, audienceType):
        self.audienceType = audienceType

    def get_audienceType(self):
        return self.audienceType

    def set_geographicArea(self, geographicArea):
        self.geographicArea = geographicArea

    def get_geographicArea(self):
        return self.geographicArea


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
