import global_data


class Thing(object):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None):
        self.additionalType = additionalType
        self.alternateName = alternateName
        self.description = description
        self.disambiguatingDescription = disambiguatingDescription
        self.identifier = identifier
        self.image = image
        self.mainEntityOfPage = mainEntityOfPage
        self.name = name
        self.potentialAction = potentialAction
        self.sameAs = sameAs
        self.url = url

    def set_additionalType(self, additionalType):
        self.additionalType = additionalType

    def get_additionalType(self):
        return self.additionalType

    def set_alternateName(self, alternateName):
        self.alternateName = alternateName

    def get_alternateName(self):
        return self.alternateName

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_disambiguatingDescription(self, disambiguatingDescription):
        self.disambiguatingDescription = disambiguatingDescription

    def get_disambiguatingDescription(self):
        return self.disambiguatingDescription

    def set_identifier(self, identifier):
        self.identifier = identifier

    def get_identifier(self):
        return self.identifier

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image

    def set_mainEntityOfPage(self, mainEntityOfPage):
        self.mainEntityOfPage = mainEntityOfPage

    def get_mainEntityOfPage(self):
        return self.mainEntityOfPage

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_potentialAction(self, potentialAction):
        self.potentialAction = potentialAction

    def get_potentialAction(self):
        return self.potentialAction

    def set_sameAs(self, sameAs):
        self.sameAs = sameAs

    def get_sameAs(self):
        return self.sameAs

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
