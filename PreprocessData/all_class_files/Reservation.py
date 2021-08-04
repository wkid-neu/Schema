from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Reservation(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, bookingTime=None, broker=None, modifiedTime=None, priceCurrency=None, programMembershipUsed=None, provider=None, reservationFor=None, reservationId=None, reservationStatus=None, reservedTicket=None, totalPrice=None, underName=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.bookingTime = bookingTime
        self.broker = broker
        self.modifiedTime = modifiedTime
        self.priceCurrency = priceCurrency
        self.programMembershipUsed = programMembershipUsed
        self.provider = provider
        self.reservationFor = reservationFor
        self.reservationId = reservationId
        self.reservationStatus = reservationStatus
        self.reservedTicket = reservedTicket
        self.totalPrice = totalPrice
        self.underName = underName

    def set_bookingTime(self, bookingTime):
        self.bookingTime = bookingTime

    def get_bookingTime(self):
        return self.bookingTime

    def set_broker(self, broker):
        self.broker = broker

    def get_broker(self):
        return self.broker

    def set_modifiedTime(self, modifiedTime):
        self.modifiedTime = modifiedTime

    def get_modifiedTime(self):
        return self.modifiedTime

    def set_priceCurrency(self, priceCurrency):
        self.priceCurrency = priceCurrency

    def get_priceCurrency(self):
        return self.priceCurrency

    def set_programMembershipUsed(self, programMembershipUsed):
        self.programMembershipUsed = programMembershipUsed

    def get_programMembershipUsed(self):
        return self.programMembershipUsed

    def set_provider(self, provider):
        self.provider = provider

    def get_provider(self):
        return self.provider

    def set_reservationFor(self, reservationFor):
        self.reservationFor = reservationFor

    def get_reservationFor(self):
        return self.reservationFor

    def set_reservationId(self, reservationId):
        self.reservationId = reservationId

    def get_reservationId(self):
        return self.reservationId

    def set_reservationStatus(self, reservationStatus):
        self.reservationStatus = reservationStatus

    def get_reservationStatus(self):
        return self.reservationStatus

    def set_reservedTicket(self, reservedTicket):
        self.reservedTicket = reservedTicket

    def get_reservedTicket(self):
        return self.reservedTicket

    def set_totalPrice(self, totalPrice):
        self.totalPrice = totalPrice

    def get_totalPrice(self):
        return self.totalPrice

    def set_underName(self, underName):
        self.underName = underName

    def get_underName(self):
        return self.underName


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
