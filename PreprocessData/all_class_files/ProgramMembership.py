from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class ProgramMembership(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, hostingOrganization=None, member=None, membershipNumber=None, programName=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.hostingOrganization = hostingOrganization
        self.member = member
        self.membershipNumber = membershipNumber
        self.programName = programName

    def set_hostingOrganization(self, hostingOrganization):
        self.hostingOrganization = hostingOrganization

    def get_hostingOrganization(self):
        return self.hostingOrganization

    def set_member(self, member):
        self.member = member

    def get_member(self):
        return self.member

    def set_membershipNumber(self, membershipNumber):
        self.membershipNumber = membershipNumber

    def get_membershipNumber(self):
        return self.membershipNumber

    def set_programName(self, programName):
        self.programName = programName

    def get_programName(self):
        return self.programName


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
