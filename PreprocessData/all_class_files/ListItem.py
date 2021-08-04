from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class ListItem(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, item=None, nextItem=None, position=None, previousItem=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.item = item
        self.nextItem = nextItem
        self.position = position
        self.previousItem = previousItem

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def set_nextItem(self, nextItem):
        self.nextItem = nextItem

    def get_nextItem(self):
        return self.nextItem

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_previousItem(self, previousItem):
        self.previousItem = previousItem

    def get_previousItem(self):
        return self.previousItem


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
