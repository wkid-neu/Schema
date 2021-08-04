from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Seat(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, seatNumber=None, seatRow=None, seatSection=None, seatingType=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.seatNumber = seatNumber
        self.seatRow = seatRow
        self.seatSection = seatSection
        self.seatingType = seatingType

    def set_seatNumber(self, seatNumber):
        self.seatNumber = seatNumber

    def get_seatNumber(self):
        return self.seatNumber

    def set_seatRow(self, seatRow):
        self.seatRow = seatRow

    def get_seatRow(self):
        return self.seatRow

    def set_seatSection(self, seatSection):
        self.seatSection = seatSection

    def get_seatSection(self):
        return self.seatSection

    def set_seatingType(self, seatingType):
        self.seatingType = seatingType

    def get_seatingType(self):
        return self.seatingType


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
