from PreprocessData.all_class_files.Reservation import Reservation
import global_data


class LodgingReservation(Reservation):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, bookingTime=None, broker=None, modifiedTime=None, priceCurrency=None, programMembershipUsed=None, provider=None, reservationFor=None, reservationId=None, reservationStatus=None, reservedTicket=None, totalPrice=None, underName=None, checkinTime=None, checkoutTime=None, lodgingUnitDescription=None, lodgingUnitType=None, numAdults=None, numChildren=None):
        Reservation.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, bookingTime, broker, modifiedTime, priceCurrency, programMembershipUsed, provider, reservationFor, reservationId, reservationStatus, reservedTicket, totalPrice, underName)
        self.checkinTime = checkinTime
        self.checkoutTime = checkoutTime
        self.lodgingUnitDescription = lodgingUnitDescription
        self.lodgingUnitType = lodgingUnitType
        self.numAdults = numAdults
        self.numChildren = numChildren

    def set_checkinTime(self, checkinTime):
        self.checkinTime = checkinTime

    def get_checkinTime(self):
        return self.checkinTime

    def set_checkoutTime(self, checkoutTime):
        self.checkoutTime = checkoutTime

    def get_checkoutTime(self):
        return self.checkoutTime

    def set_lodgingUnitDescription(self, lodgingUnitDescription):
        self.lodgingUnitDescription = lodgingUnitDescription

    def get_lodgingUnitDescription(self):
        return self.lodgingUnitDescription

    def set_lodgingUnitType(self, lodgingUnitType):
        self.lodgingUnitType = lodgingUnitType

    def get_lodgingUnitType(self):
        return self.lodgingUnitType

    def set_numAdults(self, numAdults):
        self.numAdults = numAdults

    def get_numAdults(self):
        return self.numAdults

    def set_numChildren(self, numChildren):
        self.numChildren = numChildren

    def get_numChildren(self):
        return self.numChildren


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
