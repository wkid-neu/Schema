from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class MenuItem(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, nutrition=None, offers=None, suitableForDiet=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.nutrition = nutrition
        self.offers = offers
        self.suitableForDiet = suitableForDiet

    def set_nutrition(self, nutrition):
        self.nutrition = nutrition

    def get_nutrition(self):
        return self.nutrition

    def set_offers(self, offers):
        self.offers = offers

    def get_offers(self):
        return self.offers

    def set_suitableForDiet(self, suitableForDiet):
        self.suitableForDiet = suitableForDiet

    def get_suitableForDiet(self):
        return self.suitableForDiet


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
