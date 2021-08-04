from PreprocessData.all_class_files.PeopleAudience import PeopleAudience
import global_data


class ParentAudience(PeopleAudience):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, audienceType=None, geographicArea=None, requiredGender=None, requiredMaxAge=None, requiredMinAge=None, suggestedGender=None, suggestedMaxAge=None, suggestedMinAge=None, childMaxAge=None, childMinAge=None):
        PeopleAudience.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, audienceType, geographicArea, requiredGender, requiredMaxAge, requiredMinAge, suggestedGender, suggestedMaxAge, suggestedMinAge)
        self.childMaxAge = childMaxAge
        self.childMinAge = childMinAge

    def set_childMaxAge(self, childMaxAge):
        self.childMaxAge = childMaxAge

    def get_childMaxAge(self):
        return self.childMaxAge

    def set_childMinAge(self, childMinAge):
        self.childMinAge = childMinAge

    def get_childMinAge(self):
        return self.childMinAge


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
