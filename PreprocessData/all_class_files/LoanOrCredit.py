from PreprocessData.all_class_files.FinancialProduct import FinancialProduct
import global_data


class LoanOrCredit(FinancialProduct):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, aggregateRating=None, areaServed=None, audience=None, availableChannel=None, award=None, brand=None, broker=None, category=None, hasOfferCatalog=None, hoursAvailable=None, isRelatedTo=None, isSimilarTo=None, logo=None, offers=None, provider=None, providerMobility=None, review=None, serviceOutput=None, serviceType=None, annualPercentageRate=None, feesAndCommissionsSpecification=None, interestRate=None, amount=None, loanTerm=None, requiredCollateral=None):
        FinancialProduct.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, aggregateRating, areaServed, audience, availableChannel, award, brand, broker, category, hasOfferCatalog, hoursAvailable, isRelatedTo, isSimilarTo, logo, offers, provider, providerMobility, review, serviceOutput, serviceType, annualPercentageRate, feesAndCommissionsSpecification, interestRate)
        self.amount = amount
        self.loanTerm = loanTerm
        self.requiredCollateral = requiredCollateral

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_loanTerm(self, loanTerm):
        self.loanTerm = loanTerm

    def get_loanTerm(self):
        return self.loanTerm

    def set_requiredCollateral(self, requiredCollateral):
        self.requiredCollateral = requiredCollateral

    def get_requiredCollateral(self):
        return self.requiredCollateral


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
