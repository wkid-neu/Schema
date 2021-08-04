from PreprocessData.all_class_files.PriceSpecification import PriceSpecification
import global_data


class UnitPriceSpecification(PriceSpecification):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, eligibleQuantity=None, eligibleTransactionVolume=None, maxPrice=None, minPrice=None, price=None, priceCurrency=None, validFrom=None, validThrough=None, valueAddedTaxIncluded=None, billingIncrement=None, priceType=None, referenceQuantity=None, unitCode=None, unitText=None):
        PriceSpecification.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, eligibleQuantity, eligibleTransactionVolume, maxPrice, minPrice, price, priceCurrency, validFrom, validThrough, valueAddedTaxIncluded)
        self.billingIncrement = billingIncrement
        self.priceType = priceType
        self.referenceQuantity = referenceQuantity
        self.unitCode = unitCode
        self.unitText = unitText

    def set_billingIncrement(self, billingIncrement):
        self.billingIncrement = billingIncrement

    def get_billingIncrement(self):
        return self.billingIncrement

    def set_priceType(self, priceType):
        self.priceType = priceType

    def get_priceType(self):
        return self.priceType

    def set_referenceQuantity(self, referenceQuantity):
        self.referenceQuantity = referenceQuantity

    def get_referenceQuantity(self):
        return self.referenceQuantity

    def set_unitCode(self, unitCode):
        self.unitCode = unitCode

    def get_unitCode(self):
        return self.unitCode

    def set_unitText(self, unitText):
        self.unitText = unitText

    def get_unitText(self):
        return self.unitText


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
