from PreprocessData.all_class_files.Service import Service
import global_data


class BroadcastService(Service):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, aggregateRating=None, areaServed=None, audience=None, availableChannel=None, award=None, brand=None, broker=None, category=None, hasOfferCatalog=None, hoursAvailable=None, isRelatedTo=None, isSimilarTo=None, logo=None, offers=None, provider=None, providerMobility=None, review=None, serviceOutput=None, serviceType=None, broadcastAffiliateOf=None, broadcastDisplayName=None, broadcastTimezone=None, broadcaster=None, parentService=None, videoFormat=None):
        Service.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, aggregateRating, areaServed, audience, availableChannel, award, brand, broker, category, hasOfferCatalog, hoursAvailable, isRelatedTo, isSimilarTo, logo, offers, provider, providerMobility, review, serviceOutput, serviceType)
        self.broadcastAffiliateOf = broadcastAffiliateOf
        self.broadcastDisplayName = broadcastDisplayName
        self.broadcastTimezone = broadcastTimezone
        self.broadcaster = broadcaster
        self.parentService = parentService
        self.videoFormat = videoFormat

    def set_broadcastAffiliateOf(self, broadcastAffiliateOf):
        self.broadcastAffiliateOf = broadcastAffiliateOf

    def get_broadcastAffiliateOf(self):
        return self.broadcastAffiliateOf

    def set_broadcastDisplayName(self, broadcastDisplayName):
        self.broadcastDisplayName = broadcastDisplayName

    def get_broadcastDisplayName(self):
        return self.broadcastDisplayName

    def set_broadcastTimezone(self, broadcastTimezone):
        self.broadcastTimezone = broadcastTimezone

    def get_broadcastTimezone(self):
        return self.broadcastTimezone

    def set_broadcaster(self, broadcaster):
        self.broadcaster = broadcaster

    def get_broadcaster(self):
        return self.broadcaster

    def set_parentService(self, parentService):
        self.parentService = parentService

    def get_parentService(self):
        return self.parentService

    def set_videoFormat(self, videoFormat):
        self.videoFormat = videoFormat

    def get_videoFormat(self):
        return self.videoFormat


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
