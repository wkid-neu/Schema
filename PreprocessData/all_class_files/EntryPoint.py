from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class EntryPoint(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, actionApplication=None, actionPlatform=None, contentType=None, encodingType=None, httpMethod=None, urlTemplate=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.actionApplication = actionApplication
        self.actionPlatform = actionPlatform
        self.contentType = contentType
        self.encodingType = encodingType
        self.httpMethod = httpMethod
        self.urlTemplate = urlTemplate

    def set_actionApplication(self, actionApplication):
        self.actionApplication = actionApplication

    def get_actionApplication(self):
        return self.actionApplication

    def set_actionPlatform(self, actionPlatform):
        self.actionPlatform = actionPlatform

    def get_actionPlatform(self):
        return self.actionPlatform

    def set_contentType(self, contentType):
        self.contentType = contentType

    def get_contentType(self):
        return self.contentType

    def set_encodingType(self, encodingType):
        self.encodingType = encodingType

    def get_encodingType(self):
        return self.encodingType

    def set_httpMethod(self, httpMethod):
        self.httpMethod = httpMethod

    def get_httpMethod(self):
        return self.httpMethod

    def set_urlTemplate(self, urlTemplate):
        self.urlTemplate = urlTemplate

    def get_urlTemplate(self):
        return self.urlTemplate


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
