from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class DatedMoneySpecification(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, amount=None, currency=None, endDate=None, startDate=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.amount = amount
        self.currency = currency
        self.endDate = endDate
        self.startDate = startDate

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_currency(self, currency):
        self.currency = currency

    def get_currency(self):
        return self.currency

    def set_endDate(self, endDate):
        self.endDate = endDate

    def get_endDate(self):
        return self.endDate

    def set_startDate(self, startDate):
        self.startDate = startDate

    def get_startDate(self):
        return self.startDate


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
