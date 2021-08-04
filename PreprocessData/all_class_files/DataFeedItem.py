from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class DataFeedItem(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, dateCreated=None, dateDeleted=None, dateModified=None, item=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.dateCreated = dateCreated
        self.dateDeleted = dateDeleted
        self.dateModified = dateModified
        self.item = item

    def set_dateCreated(self, dateCreated):
        self.dateCreated = dateCreated

    def get_dateCreated(self):
        return self.dateCreated

    def set_dateDeleted(self, dateDeleted):
        self.dateDeleted = dateDeleted

    def get_dateDeleted(self):
        return self.dateDeleted

    def set_dateModified(self, dateModified):
        self.dateModified = dateModified

    def get_dateModified(self):
        return self.dateModified

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
