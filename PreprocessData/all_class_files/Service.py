from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Service(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, aggregateRating=None, areaServed=None, audience=None, availableChannel=None, award=None, brand=None, broker=None, category=None, hasOfferCatalog=None, hoursAvailable=None, isRelatedTo=None, isSimilarTo=None, logo=None, offers=None, provider=None, providerMobility=None, review=None, serviceOutput=None, serviceType=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.aggregateRating = aggregateRating
        self.areaServed = areaServed
        self.audience = audience
        self.availableChannel = availableChannel
        self.award = award
        self.brand = brand
        self.broker = broker
        self.category = category
        self.hasOfferCatalog = hasOfferCatalog
        self.hoursAvailable = hoursAvailable
        self.isRelatedTo = isRelatedTo
        self.isSimilarTo = isSimilarTo
        self.logo = logo
        self.offers = offers
        self.provider = provider
        self.providerMobility = providerMobility
        self.review = review
        self.serviceOutput = serviceOutput
        self.serviceType = serviceType

    def set_aggregateRating(self, aggregateRating):
        self.aggregateRating = aggregateRating

    def get_aggregateRating(self):
        return self.aggregateRating

    def set_areaServed(self, areaServed):
        self.areaServed = areaServed

    def get_areaServed(self):
        return self.areaServed

    def set_audience(self, audience):
        self.audience = audience

    def get_audience(self):
        return self.audience

    def set_availableChannel(self, availableChannel):
        self.availableChannel = availableChannel

    def get_availableChannel(self):
        return self.availableChannel

    def set_award(self, award):
        self.award = award

    def get_award(self):
        return self.award

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_broker(self, broker):
        self.broker = broker

    def get_broker(self):
        return self.broker

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_hasOfferCatalog(self, hasOfferCatalog):
        self.hasOfferCatalog = hasOfferCatalog

    def get_hasOfferCatalog(self):
        return self.hasOfferCatalog

    def set_hoursAvailable(self, hoursAvailable):
        self.hoursAvailable = hoursAvailable

    def get_hoursAvailable(self):
        return self.hoursAvailable

    def set_isRelatedTo(self, isRelatedTo):
        self.isRelatedTo = isRelatedTo

    def get_isRelatedTo(self):
        return self.isRelatedTo

    def set_isSimilarTo(self, isSimilarTo):
        self.isSimilarTo = isSimilarTo

    def get_isSimilarTo(self):
        return self.isSimilarTo

    def set_logo(self, logo):
        self.logo = logo

    def get_logo(self):
        return self.logo

    def set_offers(self, offers):
        self.offers = offers

    def get_offers(self):
        return self.offers

    def set_provider(self, provider):
        self.provider = provider

    def get_provider(self):
        return self.provider

    def set_providerMobility(self, providerMobility):
        self.providerMobility = providerMobility

    def get_providerMobility(self):
        return self.providerMobility

    def set_review(self, review):
        self.review = review

    def get_review(self):
        return self.review

    def set_serviceOutput(self, serviceOutput):
        self.serviceOutput = serviceOutput

    def get_serviceOutput(self):
        return self.serviceOutput

    def set_serviceType(self, serviceType):
        self.serviceType = serviceType

    def get_serviceType(self):
        return self.serviceType


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
