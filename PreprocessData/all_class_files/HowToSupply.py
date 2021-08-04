from PreprocessData.all_class_files.HowToItem import HowToItem
import global_data


class HowToSupply(HowToItem):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, item=None, nextItem=None, position=None, previousItem=None, requiredQuantity=None, estimatedCost=None):
        HowToItem.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, item, nextItem, position, previousItem, requiredQuantity)
        self.estimatedCost = estimatedCost

    def set_estimatedCost(self, estimatedCost):
        self.estimatedCost = estimatedCost

    def get_estimatedCost(self):
        return self.estimatedCost


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
