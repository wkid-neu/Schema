from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class PriceSpecification(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, eligibleQuantity=None, eligibleTransactionVolume=None, maxPrice=None, minPrice=None, price=None, priceCurrency=None, validFrom=None, validThrough=None, valueAddedTaxIncluded=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.eligibleQuantity = eligibleQuantity
        self.eligibleTransactionVolume = eligibleTransactionVolume
        self.maxPrice = maxPrice
        self.minPrice = minPrice
        self.price = price
        self.priceCurrency = priceCurrency
        self.validFrom = validFrom
        self.validThrough = validThrough
        self.valueAddedTaxIncluded = valueAddedTaxIncluded

    def set_eligibleQuantity(self, eligibleQuantity):
        self.eligibleQuantity = eligibleQuantity

    def get_eligibleQuantity(self):
        return self.eligibleQuantity

    def set_eligibleTransactionVolume(self, eligibleTransactionVolume):
        self.eligibleTransactionVolume = eligibleTransactionVolume

    def get_eligibleTransactionVolume(self):
        return self.eligibleTransactionVolume

    def set_maxPrice(self, maxPrice):
        self.maxPrice = maxPrice

    def get_maxPrice(self):
        return self.maxPrice

    def set_minPrice(self, minPrice):
        self.minPrice = minPrice

    def get_minPrice(self):
        return self.minPrice

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_priceCurrency(self, priceCurrency):
        self.priceCurrency = priceCurrency

    def get_priceCurrency(self):
        return self.priceCurrency

    def set_validFrom(self, validFrom):
        self.validFrom = validFrom

    def get_validFrom(self):
        return self.validFrom

    def set_validThrough(self, validThrough):
        self.validThrough = validThrough

    def get_validThrough(self):
        return self.validThrough

    def set_valueAddedTaxIncluded(self, valueAddedTaxIncluded):
        self.valueAddedTaxIncluded = valueAddedTaxIncluded

    def get_valueAddedTaxIncluded(self):
        return self.valueAddedTaxIncluded


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
