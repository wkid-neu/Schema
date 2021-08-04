from PreprocessData.all_class_files.Offer import Offer
import global_data


class AggregateOffer(Offer):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, acceptedPaymentMethod=None, addOn=None, advanceBookingRequirement=None, aggregateRating=None, areaServed=None, availability=None, availabilityEnds=None, availabilityStarts=None, availableAtOrFrom=None, availableDeliveryMethod=None, businessFunction=None, category=None, deliveryLeadTime=None, eligibleCustomerType=None, eligibleDuration=None, eligibleQuantity=None, eligibleRegion=None, eligibleTransactionVolume=None, gtin12=None, gtin13=None, gtin14=None, gtin8=None, includesObject=None, ineligibleRegion=None, inventoryLevel=None, itemCondition=None, itemOffered=None, mpn=None, offeredBy=None, price=None, priceCurrency=None, priceSpecification=None, priceValidUntil=None, review=None, seller=None, serialNumber=None, sku=None, validFrom=None, validThrough=None, warranty=None, highPrice=None, lowPrice=None, offerCount=None, offers=None):
        Offer.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, acceptedPaymentMethod, addOn, advanceBookingRequirement, aggregateRating, areaServed, availability, availabilityEnds, availabilityStarts, availableAtOrFrom, availableDeliveryMethod, businessFunction, category, deliveryLeadTime, eligibleCustomerType, eligibleDuration, eligibleQuantity, eligibleRegion, eligibleTransactionVolume, gtin12, gtin13, gtin14, gtin8, includesObject, ineligibleRegion, inventoryLevel, itemCondition, itemOffered, mpn, offeredBy, price, priceCurrency, priceSpecification, priceValidUntil, review, seller, serialNumber, sku, validFrom, validThrough, warranty)
        self.highPrice = highPrice
        self.lowPrice = lowPrice
        self.offerCount = offerCount
        self.offers = offers

    def set_highPrice(self, highPrice):
        self.highPrice = highPrice

    def get_highPrice(self):
        return self.highPrice

    def set_lowPrice(self, lowPrice):
        self.lowPrice = lowPrice

    def get_lowPrice(self):
        return self.lowPrice

    def set_offerCount(self, offerCount):
        self.offerCount = offerCount

    def get_offerCount(self):
        return self.offerCount

    def set_offers(self, offers):
        self.offers = offers

    def get_offers(self):
        return self.offers


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
