from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class WarrantyPromise(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, durationOfWarranty=None, warrantyScope=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.durationOfWarranty = durationOfWarranty
        self.warrantyScope = warrantyScope

    def set_durationOfWarranty(self, durationOfWarranty):
        self.durationOfWarranty = durationOfWarranty

    def get_durationOfWarranty(self):
        return self.durationOfWarranty

    def set_warrantyScope(self, warrantyScope):
        self.warrantyScope = warrantyScope

    def get_warrantyScope(self):
        return self.warrantyScope


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
