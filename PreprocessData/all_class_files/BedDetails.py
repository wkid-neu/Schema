from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class BedDetails(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, numberOfBeds=None, typeOfBed=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.numberOfBeds = numberOfBeds
        self.typeOfBed = typeOfBed

    def set_numberOfBeds(self, numberOfBeds):
        self.numberOfBeds = numberOfBeds

    def get_numberOfBeds(self):
        return self.numberOfBeds

    def set_typeOfBed(self, typeOfBed):
        self.typeOfBed = typeOfBed

    def get_typeOfBed(self):
        return self.typeOfBed


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
