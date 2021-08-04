from PreprocessData.all_class_files.Audience import Audience
import global_data


class PeopleAudience(Audience):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, audienceType=None, geographicArea=None, requiredGender=None, requiredMaxAge=None, requiredMinAge=None, suggestedGender=None, suggestedMaxAge=None, suggestedMinAge=None):
        Audience.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, audienceType, geographicArea)
        self.requiredGender = requiredGender
        self.requiredMaxAge = requiredMaxAge
        self.requiredMinAge = requiredMinAge
        self.suggestedGender = suggestedGender
        self.suggestedMaxAge = suggestedMaxAge
        self.suggestedMinAge = suggestedMinAge

    def set_requiredGender(self, requiredGender):
        self.requiredGender = requiredGender

    def get_requiredGender(self):
        return self.requiredGender

    def set_requiredMaxAge(self, requiredMaxAge):
        self.requiredMaxAge = requiredMaxAge

    def get_requiredMaxAge(self):
        return self.requiredMaxAge

    def set_requiredMinAge(self, requiredMinAge):
        self.requiredMinAge = requiredMinAge

    def get_requiredMinAge(self):
        return self.requiredMinAge

    def set_suggestedGender(self, suggestedGender):
        self.suggestedGender = suggestedGender

    def get_suggestedGender(self):
        return self.suggestedGender

    def set_suggestedMaxAge(self, suggestedMaxAge):
        self.suggestedMaxAge = suggestedMaxAge

    def get_suggestedMaxAge(self):
        return self.suggestedMaxAge

    def set_suggestedMinAge(self, suggestedMinAge):
        self.suggestedMinAge = suggestedMinAge

    def get_suggestedMinAge(self):
        return self.suggestedMinAge


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
