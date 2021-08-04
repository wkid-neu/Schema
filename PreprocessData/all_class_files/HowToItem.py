from PreprocessData.all_class_files.ListItem import ListItem
import global_data


class HowToItem(ListItem):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, item=None, nextItem=None, position=None, previousItem=None, requiredQuantity=None):
        ListItem.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, item, nextItem, position, previousItem)
        self.requiredQuantity = requiredQuantity

    def set_requiredQuantity(self, requiredQuantity):
        self.requiredQuantity = requiredQuantity

    def get_requiredQuantity(self):
        return self.requiredQuantity


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
