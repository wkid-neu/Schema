from PreprocessData.all_class_files.Service import Service
import global_data


class FinancialProduct(Service):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, aggregateRating=None, areaServed=None, audience=None, availableChannel=None, award=None, brand=None, broker=None, category=None, hasOfferCatalog=None, hoursAvailable=None, isRelatedTo=None, isSimilarTo=None, logo=None, offers=None, provider=None, providerMobility=None, review=None, serviceOutput=None, serviceType=None, annualPercentageRate=None, feesAndCommissionsSpecification=None, interestRate=None):
        Service.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, aggregateRating, areaServed, audience, availableChannel, award, brand, broker, category, hasOfferCatalog, hoursAvailable, isRelatedTo, isSimilarTo, logo, offers, provider, providerMobility, review, serviceOutput, serviceType)
        self.annualPercentageRate = annualPercentageRate
        self.feesAndCommissionsSpecification = feesAndCommissionsSpecification
        self.interestRate = interestRate

    def set_annualPercentageRate(self, annualPercentageRate):
        self.annualPercentageRate = annualPercentageRate

    def get_annualPercentageRate(self):
        return self.annualPercentageRate

    def set_feesAndCommissionsSpecification(self, feesAndCommissionsSpecification):
        self.feesAndCommissionsSpecification = feesAndCommissionsSpecification

    def get_feesAndCommissionsSpecification(self):
        return self.feesAndCommissionsSpecification

    def set_interestRate(self, interestRate):
        self.interestRate = interestRate

    def get_interestRate(self):
        return self.interestRate


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
