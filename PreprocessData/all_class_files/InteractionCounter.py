from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class InteractionCounter(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, interactionService=None, interactionType=None, userInteractionCount=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.interactionService = interactionService
        self.interactionType = interactionType
        self.userInteractionCount = userInteractionCount

    def set_interactionService(self, interactionService):
        self.interactionService = interactionService

    def get_interactionService(self):
        return self.interactionService

    def set_interactionType(self, interactionType):
        self.interactionType = interactionType

    def get_interactionType(self):
        return self.interactionType

    def set_userInteractionCount(self, userInteractionCount):
        self.userInteractionCount = userInteractionCount

    def get_userInteractionCount(self):
        return self.userInteractionCount


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
