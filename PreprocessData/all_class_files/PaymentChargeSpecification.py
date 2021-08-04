from PreprocessData.all_class_files.PriceSpecification import PriceSpecification
import global_data


class PaymentChargeSpecification(PriceSpecification):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, eligibleQuantity=None, eligibleTransactionVolume=None, maxPrice=None, minPrice=None, price=None, priceCurrency=None, validFrom=None, validThrough=None, valueAddedTaxIncluded=None, appliesToDeliveryMethod=None, appliesToPaymentMethod=None):
        PriceSpecification.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, eligibleQuantity, eligibleTransactionVolume, maxPrice, minPrice, price, priceCurrency, validFrom, validThrough, valueAddedTaxIncluded)
        self.appliesToDeliveryMethod = appliesToDeliveryMethod
        self.appliesToPaymentMethod = appliesToPaymentMethod

    def set_appliesToDeliveryMethod(self, appliesToDeliveryMethod):
        self.appliesToDeliveryMethod = appliesToDeliveryMethod

    def get_appliesToDeliveryMethod(self):
        return self.appliesToDeliveryMethod

    def set_appliesToPaymentMethod(self, appliesToPaymentMethod):
        self.appliesToPaymentMethod = appliesToPaymentMethod

    def get_appliesToPaymentMethod(self):
        return self.appliesToPaymentMethod


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
