from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Rating(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, author=None, bestRating=None, ratingValue=None, worstRating=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.author = author
        self.bestRating = bestRating
        self.ratingValue = ratingValue
        self.worstRating = worstRating

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_bestRating(self, bestRating):
        self.bestRating = bestRating

    def get_bestRating(self):
        return self.bestRating

    def set_ratingValue(self, ratingValue):
        self.ratingValue = ratingValue

    def get_ratingValue(self):
        return self.ratingValue

    def set_worstRating(self, worstRating):
        self.worstRating = worstRating

    def get_worstRating(self):
        return self.worstRating


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
