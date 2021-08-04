from PreprocessData.all_class_files.Reservation import Reservation
import global_data


class ReservationPackage(Reservation):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, bookingTime=None, broker=None, modifiedTime=None, priceCurrency=None, programMembershipUsed=None, provider=None, reservationFor=None, reservationId=None, reservationStatus=None, reservedTicket=None, totalPrice=None, underName=None, subReservation=None):
        Reservation.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, bookingTime, broker, modifiedTime, priceCurrency, programMembershipUsed, provider, reservationFor, reservationId, reservationStatus, reservedTicket, totalPrice, underName)
        self.subReservation = subReservation

    def set_subReservation(self, subReservation):
        self.subReservation = subReservation

    def get_subReservation(self):
        return self.subReservation


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
