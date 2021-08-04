from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Demand(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, acceptedPaymentMethod=None, advanceBookingRequirement=None, areaServed=None, availability=None, availabilityEnds=None, availabilityStarts=None, availableAtOrFrom=None, availableDeliveryMethod=None, businessFunction=None, deliveryLeadTime=None, eligibleCustomerType=None, eligibleDuration=None, eligibleQuantity=None, eligibleRegion=None, eligibleTransactionVolume=None, gtin12=None, gtin13=None, gtin14=None, gtin8=None, includesObject=None, ineligibleRegion=None, inventoryLevel=None, itemCondition=None, itemOffered=None, mpn=None, priceSpecification=None, seller=None, serialNumber=None, sku=None, validFrom=None, validThrough=None, warranty=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.acceptedPaymentMethod = acceptedPaymentMethod
        self.advanceBookingRequirement = advanceBookingRequirement
        self.areaServed = areaServed
        self.availability = availability
        self.availabilityEnds = availabilityEnds
        self.availabilityStarts = availabilityStarts
        self.availableAtOrFrom = availableAtOrFrom
        self.availableDeliveryMethod = availableDeliveryMethod
        self.businessFunction = businessFunction
        self.deliveryLeadTime = deliveryLeadTime
        self.eligibleCustomerType = eligibleCustomerType
        self.eligibleDuration = eligibleDuration
        self.eligibleQuantity = eligibleQuantity
        self.eligibleRegion = eligibleRegion
        self.eligibleTransactionVolume = eligibleTransactionVolume
        self.gtin12 = gtin12
        self.gtin13 = gtin13
        self.gtin14 = gtin14
        self.gtin8 = gtin8
        self.includesObject = includesObject
        self.ineligibleRegion = ineligibleRegion
        self.inventoryLevel = inventoryLevel
        self.itemCondition = itemCondition
        self.itemOffered = itemOffered
        self.mpn = mpn
        self.priceSpecification = priceSpecification
        self.seller = seller
        self.serialNumber = serialNumber
        self.sku = sku
        self.validFrom = validFrom
        self.validThrough = validThrough
        self.warranty = warranty

    def set_acceptedPaymentMethod(self, acceptedPaymentMethod):
        self.acceptedPaymentMethod = acceptedPaymentMethod

    def get_acceptedPaymentMethod(self):
        return self.acceptedPaymentMethod

    def set_advanceBookingRequirement(self, advanceBookingRequirement):
        self.advanceBookingRequirement = advanceBookingRequirement

    def get_advanceBookingRequirement(self):
        return self.advanceBookingRequirement

    def set_areaServed(self, areaServed):
        self.areaServed = areaServed

    def get_areaServed(self):
        return self.areaServed

    def set_availability(self, availability):
        self.availability = availability

    def get_availability(self):
        return self.availability

    def set_availabilityEnds(self, availabilityEnds):
        self.availabilityEnds = availabilityEnds

    def get_availabilityEnds(self):
        return self.availabilityEnds

    def set_availabilityStarts(self, availabilityStarts):
        self.availabilityStarts = availabilityStarts

    def get_availabilityStarts(self):
        return self.availabilityStarts

    def set_availableAtOrFrom(self, availableAtOrFrom):
        self.availableAtOrFrom = availableAtOrFrom

    def get_availableAtOrFrom(self):
        return self.availableAtOrFrom

    def set_availableDeliveryMethod(self, availableDeliveryMethod):
        self.availableDeliveryMethod = availableDeliveryMethod

    def get_availableDeliveryMethod(self):
        return self.availableDeliveryMethod

    def set_businessFunction(self, businessFunction):
        self.businessFunction = businessFunction

    def get_businessFunction(self):
        return self.businessFunction

    def set_deliveryLeadTime(self, deliveryLeadTime):
        self.deliveryLeadTime = deliveryLeadTime

    def get_deliveryLeadTime(self):
        return self.deliveryLeadTime

    def set_eligibleCustomerType(self, eligibleCustomerType):
        self.eligibleCustomerType = eligibleCustomerType

    def get_eligibleCustomerType(self):
        return self.eligibleCustomerType

    def set_eligibleDuration(self, eligibleDuration):
        self.eligibleDuration = eligibleDuration

    def get_eligibleDuration(self):
        return self.eligibleDuration

    def set_eligibleQuantity(self, eligibleQuantity):
        self.eligibleQuantity = eligibleQuantity

    def get_eligibleQuantity(self):
        return self.eligibleQuantity

    def set_eligibleRegion(self, eligibleRegion):
        self.eligibleRegion = eligibleRegion

    def get_eligibleRegion(self):
        return self.eligibleRegion

    def set_eligibleTransactionVolume(self, eligibleTransactionVolume):
        self.eligibleTransactionVolume = eligibleTransactionVolume

    def get_eligibleTransactionVolume(self):
        return self.eligibleTransactionVolume

    def set_gtin12(self, gtin12):
        self.gtin12 = gtin12

    def get_gtin12(self):
        return self.gtin12

    def set_gtin13(self, gtin13):
        self.gtin13 = gtin13

    def get_gtin13(self):
        return self.gtin13

    def set_gtin14(self, gtin14):
        self.gtin14 = gtin14

    def get_gtin14(self):
        return self.gtin14

    def set_gtin8(self, gtin8):
        self.gtin8 = gtin8

    def get_gtin8(self):
        return self.gtin8

    def set_includesObject(self, includesObject):
        self.includesObject = includesObject

    def get_includesObject(self):
        return self.includesObject

    def set_ineligibleRegion(self, ineligibleRegion):
        self.ineligibleRegion = ineligibleRegion

    def get_ineligibleRegion(self):
        return self.ineligibleRegion

    def set_inventoryLevel(self, inventoryLevel):
        self.inventoryLevel = inventoryLevel

    def get_inventoryLevel(self):
        return self.inventoryLevel

    def set_itemCondition(self, itemCondition):
        self.itemCondition = itemCondition

    def get_itemCondition(self):
        return self.itemCondition

    def set_itemOffered(self, itemOffered):
        self.itemOffered = itemOffered

    def get_itemOffered(self):
        return self.itemOffered

    def set_mpn(self, mpn):
        self.mpn = mpn

    def get_mpn(self):
        return self.mpn

    def set_priceSpecification(self, priceSpecification):
        self.priceSpecification = priceSpecification

    def get_priceSpecification(self):
        return self.priceSpecification

    def set_seller(self, seller):
        self.seller = seller

    def get_seller(self):
        return self.seller

    def set_serialNumber(self, serialNumber):
        self.serialNumber = serialNumber

    def get_serialNumber(self):
        return self.serialNumber

    def set_sku(self, sku):
        self.sku = sku

    def get_sku(self):
        return self.sku

    def set_validFrom(self, validFrom):
        self.validFrom = validFrom

    def get_validFrom(self):
        return self.validFrom

    def set_validThrough(self, validThrough):
        self.validThrough = validThrough

    def get_validThrough(self):
        return self.validThrough

    def set_warranty(self, warranty):
        self.warranty = warranty

    def get_warranty(self):
        return self.warranty


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
