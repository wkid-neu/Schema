from PreprocessData.all_class_files.FinancialProduct import FinancialProduct
import global_data


class PaymentService(FinancialProduct):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, aggregateRating=None, areaServed=None, audience=None, availableChannel=None, award=None, brand=None, broker=None, category=None, hasOfferCatalog=None, hoursAvailable=None, isRelatedTo=None, isSimilarTo=None, logo=None, offers=None, provider=None, providerMobility=None, review=None, serviceOutput=None, serviceType=None, annualPercentageRate=None, feesAndCommissionsSpecification=None, interestRate=None):
        FinancialProduct.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, aggregateRating, areaServed, audience, availableChannel, award, brand, broker, category, hasOfferCatalog, hoursAvailable, isRelatedTo, isSimilarTo, logo, offers, provider, providerMobility, review, serviceOutput, serviceType, annualPercentageRate, feesAndCommissionsSpecification, interestRate)
