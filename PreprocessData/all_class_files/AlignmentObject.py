from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class AlignmentObject(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, alignmentType=None, educationalFramework=None, targetDescription=None, targetName=None, targetUrl=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.alignmentType = alignmentType
        self.educationalFramework = educationalFramework
        self.targetDescription = targetDescription
        self.targetName = targetName
        self.targetUrl = targetUrl

    def set_alignmentType(self, alignmentType):
        self.alignmentType = alignmentType

    def get_alignmentType(self):
        return self.alignmentType

    def set_educationalFramework(self, educationalFramework):
        self.educationalFramework = educationalFramework

    def get_educationalFramework(self):
        return self.educationalFramework

    def set_targetDescription(self, targetDescription):
        self.targetDescription = targetDescription

    def get_targetDescription(self):
        return self.targetDescription

    def set_targetName(self, targetName):
        self.targetName = targetName

    def get_targetName(self):
        return self.targetName

    def set_targetUrl(self, targetUrl):
        self.targetUrl = targetUrl

    def get_targetUrl(self):
        return self.targetUrl


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
