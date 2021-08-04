from PreprocessData.all_class_files.Reservation import Reservation
import global_data


class FlightReservation(Reservation):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, bookingTime=None, broker=None, modifiedTime=None, priceCurrency=None, programMembershipUsed=None, provider=None, reservationFor=None, reservationId=None, reservationStatus=None, reservedTicket=None, totalPrice=None, underName=None, boardingGroup=None, passengerPriorityStatus=None, passengerSequenceNumber=None, securityScreening=None):
        Reservation.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, bookingTime, broker, modifiedTime, priceCurrency, programMembershipUsed, provider, reservationFor, reservationId, reservationStatus, reservedTicket, totalPrice, underName)
        self.boardingGroup = boardingGroup
        self.passengerPriorityStatus = passengerPriorityStatus
        self.passengerSequenceNumber = passengerSequenceNumber
        self.securityScreening = securityScreening

    def set_boardingGroup(self, boardingGroup):
        self.boardingGroup = boardingGroup

    def get_boardingGroup(self):
        return self.boardingGroup

    def set_passengerPriorityStatus(self, passengerPriorityStatus):
        self.passengerPriorityStatus = passengerPriorityStatus

    def get_passengerPriorityStatus(self):
        return self.passengerPriorityStatus

    def set_passengerSequenceNumber(self, passengerSequenceNumber):
        self.passengerSequenceNumber = passengerSequenceNumber

    def get_passengerSequenceNumber(self):
        return self.passengerSequenceNumber

    def set_securityScreening(self, securityScreening):
        self.securityScreening = securityScreening

    def get_securityScreening(self):
        return self.securityScreening


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
