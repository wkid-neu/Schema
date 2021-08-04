from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class ParcelDelivery(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, deliveryAddress=None, deliveryStatus=None, expectedArrivalFrom=None, expectedArrivalUntil=None, hasDeliveryMethod=None, itemShipped=None, originAddress=None, partOfOrder=None, provider=None, trackingNumber=None, trackingUrl=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.deliveryAddress = deliveryAddress
        self.deliveryStatus = deliveryStatus
        self.expectedArrivalFrom = expectedArrivalFrom
        self.expectedArrivalUntil = expectedArrivalUntil
        self.hasDeliveryMethod = hasDeliveryMethod
        self.itemShipped = itemShipped
        self.originAddress = originAddress
        self.partOfOrder = partOfOrder
        self.provider = provider
        self.trackingNumber = trackingNumber
        self.trackingUrl = trackingUrl

    def set_deliveryAddress(self, deliveryAddress):
        self.deliveryAddress = deliveryAddress

    def get_deliveryAddress(self):
        return self.deliveryAddress

    def set_deliveryStatus(self, deliveryStatus):
        self.deliveryStatus = deliveryStatus

    def get_deliveryStatus(self):
        return self.deliveryStatus

    def set_expectedArrivalFrom(self, expectedArrivalFrom):
        self.expectedArrivalFrom = expectedArrivalFrom

    def get_expectedArrivalFrom(self):
        return self.expectedArrivalFrom

    def set_expectedArrivalUntil(self, expectedArrivalUntil):
        self.expectedArrivalUntil = expectedArrivalUntil

    def get_expectedArrivalUntil(self):
        return self.expectedArrivalUntil

    def set_hasDeliveryMethod(self, hasDeliveryMethod):
        self.hasDeliveryMethod = hasDeliveryMethod

    def get_hasDeliveryMethod(self):
        return self.hasDeliveryMethod

    def set_itemShipped(self, itemShipped):
        self.itemShipped = itemShipped

    def get_itemShipped(self):
        return self.itemShipped

    def set_originAddress(self, originAddress):
        self.originAddress = originAddress

    def get_originAddress(self):
        return self.originAddress

    def set_partOfOrder(self, partOfOrder):
        self.partOfOrder = partOfOrder

    def get_partOfOrder(self):
        return self.partOfOrder

    def set_provider(self, provider):
        self.provider = provider

    def get_provider(self):
        return self.provider

    def set_trackingNumber(self, trackingNumber):
        self.trackingNumber = trackingNumber

    def get_trackingNumber(self):
        return self.trackingNumber

    def set_trackingUrl(self, trackingUrl):
        self.trackingUrl = trackingUrl

    def get_trackingUrl(self):
        return self.trackingUrl


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
