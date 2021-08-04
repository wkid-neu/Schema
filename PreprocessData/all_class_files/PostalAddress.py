from PreprocessData.all_class_files.ContactPoint import ContactPoint
import global_data


class PostalAddress(ContactPoint):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, areaServed=None, availableLanguage=None, contactOption=None, contactType=None, email=None, faxNumber=None, hoursAvailable=None, productSupported=None, telephone=None, addressCountry=None, addressLocality=None, addressRegion=None, postOfficeBoxNumber=None, postalCode=None, streetAddress=None):
        ContactPoint.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, areaServed, availableLanguage, contactOption, contactType, email, faxNumber, hoursAvailable, productSupported, telephone)
        self.addressCountry = addressCountry
        self.addressLocality = addressLocality
        self.addressRegion = addressRegion
        self.postOfficeBoxNumber = postOfficeBoxNumber
        self.postalCode = postalCode
        self.streetAddress = streetAddress

    def set_addressCountry(self, addressCountry):
        self.addressCountry = addressCountry

    def get_addressCountry(self):
        return self.addressCountry

    def set_addressLocality(self, addressLocality):
        self.addressLocality = addressLocality

    def get_addressLocality(self):
        return self.addressLocality

    def set_addressRegion(self, addressRegion):
        self.addressRegion = addressRegion

    def get_addressRegion(self):
        return self.addressRegion

    def set_postOfficeBoxNumber(self, postOfficeBoxNumber):
        self.postOfficeBoxNumber = postOfficeBoxNumber

    def get_postOfficeBoxNumber(self):
        return self.postOfficeBoxNumber

    def set_postalCode(self, postalCode):
        self.postalCode = postalCode

    def get_postalCode(self):
        return self.postalCode

    def set_streetAddress(self, streetAddress):
        self.streetAddress = streetAddress

    def get_streetAddress(self):
        return self.streetAddress


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
