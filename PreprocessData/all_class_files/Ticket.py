from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Ticket(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, dateIssued=None, issuedBy=None, priceCurrency=None, ticketNumber=None, ticketToken=None, ticketedSeat=None, totalPrice=None, underName=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.dateIssued = dateIssued
        self.issuedBy = issuedBy
        self.priceCurrency = priceCurrency
        self.ticketNumber = ticketNumber
        self.ticketToken = ticketToken
        self.ticketedSeat = ticketedSeat
        self.totalPrice = totalPrice
        self.underName = underName

    def set_dateIssued(self, dateIssued):
        self.dateIssued = dateIssued

    def get_dateIssued(self):
        return self.dateIssued

    def set_issuedBy(self, issuedBy):
        self.issuedBy = issuedBy

    def get_issuedBy(self):
        return self.issuedBy

    def set_priceCurrency(self, priceCurrency):
        self.priceCurrency = priceCurrency

    def get_priceCurrency(self):
        return self.priceCurrency

    def set_ticketNumber(self, ticketNumber):
        self.ticketNumber = ticketNumber

    def get_ticketNumber(self):
        return self.ticketNumber

    def set_ticketToken(self, ticketToken):
        self.ticketToken = ticketToken

    def get_ticketToken(self):
        return self.ticketToken

    def set_ticketedSeat(self, ticketedSeat):
        self.ticketedSeat = ticketedSeat

    def get_ticketedSeat(self):
        return self.ticketedSeat

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
