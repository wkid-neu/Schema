from PreprocessData.all_class_files.Rating import Rating
import global_data


class AggregateRating(Rating):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, author=None, bestRating=None, ratingValue=None, worstRating=None, itemReviewed=None, ratingCount=None, reviewCount=None):
        Rating.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, author, bestRating, ratingValue, worstRating)
        self.itemReviewed = itemReviewed
        self.ratingCount = ratingCount
        self.reviewCount = reviewCount

    def set_itemReviewed(self, itemReviewed):
        self.itemReviewed = itemReviewed

    def get_itemReviewed(self):
        return self.itemReviewed

    def set_ratingCount(self, ratingCount):
        self.ratingCount = ratingCount

    def get_ratingCount(self):
        return self.ratingCount

    def set_reviewCount(self, reviewCount):
        self.reviewCount = reviewCount

    def get_reviewCount(self):
        return self.reviewCount


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
