from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class ContactPoint(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, areaServed=None, availableLanguage=None, contactOption=None, contactType=None, email=None, faxNumber=None, hoursAvailable=None, productSupported=None, telephone=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.areaServed = areaServed
        self.availableLanguage = availableLanguage
        self.contactOption = contactOption
        self.contactType = contactType
        self.email = email
        self.faxNumber = faxNumber
        self.hoursAvailable = hoursAvailable
        self.productSupported = productSupported
        self.telephone = telephone

    def set_areaServed(self, areaServed):
        self.areaServed = areaServed

    def get_areaServed(self):
        return self.areaServed

    def set_availableLanguage(self, availableLanguage):
        self.availableLanguage = availableLanguage

    def get_availableLanguage(self):
        return self.availableLanguage

    def set_contactOption(self, contactOption):
        self.contactOption = contactOption

    def get_contactOption(self):
        return self.contactOption

    def set_contactType(self, contactType):
        self.contactType = contactType

    def get_contactType(self):
        return self.contactType

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_faxNumber(self, faxNumber):
        self.faxNumber = faxNumber

    def get_faxNumber(self):
        return self.faxNumber

    def set_hoursAvailable(self, hoursAvailable):
        self.hoursAvailable = hoursAvailable

    def get_hoursAvailable(self):
        return self.hoursAvailable

    def set_productSupported(self, productSupported):
        self.productSupported = productSupported

    def get_productSupported(self):
        return self.productSupported

    def set_telephone(self, telephone):
        self.telephone = telephone

    def get_telephone(self):
        return self.telephone


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
