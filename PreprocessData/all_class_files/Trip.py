from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Trip(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, arrivalTime=None, departureTime=None, offers=None, provider=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.arrivalTime = arrivalTime
        self.departureTime = departureTime
        self.offers = offers
        self.provider = provider

    def set_arrivalTime(self, arrivalTime):
        self.arrivalTime = arrivalTime

    def get_arrivalTime(self):
        return self.arrivalTime

    def set_departureTime(self, departureTime):
        self.departureTime = departureTime

    def get_departureTime(self):
        return self.departureTime

    def set_offers(self, offers):
        self.offers = offers

    def get_offers(self):
        return self.offers

    def set_provider(self, provider):
        self.provider = provider

    def get_provider(self):
        return self.provider


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
