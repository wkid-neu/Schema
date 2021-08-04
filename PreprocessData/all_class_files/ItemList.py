from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class ItemList(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, itemListElement=None, itemListOrder=None, numberOfItems=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.itemListElement = itemListElement
        self.itemListOrder = itemListOrder
        self.numberOfItems = numberOfItems

    def set_itemListElement(self, itemListElement):
        self.itemListElement = itemListElement

    def get_itemListElement(self):
        return self.itemListElement

    def set_itemListOrder(self, itemListOrder):
        self.itemListOrder = itemListOrder

    def get_itemListOrder(self):
        return self.itemListOrder

    def set_numberOfItems(self, numberOfItems):
        self.numberOfItems = numberOfItems

    def get_numberOfItems(self):
        return self.numberOfItems


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
