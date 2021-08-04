from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class ServiceChannel(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, availableLanguage=None, processingTime=None, providesService=None, serviceLocation=None, servicePhone=None, servicePostalAddress=None, serviceSmsNumber=None, serviceUrl=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.availableLanguage = availableLanguage
        self.processingTime = processingTime
        self.providesService = providesService
        self.serviceLocation = serviceLocation
        self.servicePhone = servicePhone
        self.servicePostalAddress = servicePostalAddress
        self.serviceSmsNumber = serviceSmsNumber
        self.serviceUrl = serviceUrl

    def set_availableLanguage(self, availableLanguage):
        self.availableLanguage = availableLanguage

    def get_availableLanguage(self):
        return self.availableLanguage

    def set_processingTime(self, processingTime):
        self.processingTime = processingTime

    def get_processingTime(self):
        return self.processingTime

    def set_providesService(self, providesService):
        self.providesService = providesService

    def get_providesService(self):
        return self.providesService

    def set_serviceLocation(self, serviceLocation):
        self.serviceLocation = serviceLocation

    def get_serviceLocation(self):
        return self.serviceLocation

    def set_servicePhone(self, servicePhone):
        self.servicePhone = servicePhone

    def get_servicePhone(self):
        return self.servicePhone

    def set_servicePostalAddress(self, servicePostalAddress):
        self.servicePostalAddress = servicePostalAddress

    def get_servicePostalAddress(self):
        return self.servicePostalAddress

    def set_serviceSmsNumber(self, serviceSmsNumber):
        self.serviceSmsNumber = serviceSmsNumber

    def get_serviceSmsNumber(self):
        return self.serviceSmsNumber

    def set_serviceUrl(self, serviceUrl):
        self.serviceUrl = serviceUrl

    def get_serviceUrl(self):
        return self.serviceUrl


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
