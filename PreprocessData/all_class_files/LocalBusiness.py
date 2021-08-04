from PreprocessData.all_class_files.Organization import Organization
from PreprocessData.all_class_files.Place import Place
import global_data


class LocalBusiness(Organization,Place):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, address=None, aggregateRating=None, alumni=None, areaServed=None, award=None, brand=None, contactPoint=None, department=None, dissolutionDate=None, duns=None, email=None, employee=None, event=None, faxNumber=None, founder=None, foundingDate=None, foundingLocation=None, funder=None, globalLocationNumber=None, hasOfferCatalog=None, hasPOS=None, isicV4=None, legalName=None, leiCode=None, location=None, logo=None, makesOffer=None, member=None, memberOf=None, naics=None, numberOfEmployees=None, owns=None, parentOrganization=None, publishingPrinciples=None, review=None, seeks=None, sponsor=None, subOrganization=None, taxID=None, telephone=None, vatID=None, additionalProperty=None, amenityFeature=None, branchCode=None, containedInPlace=None, containsPlace=None, geo=None, hasMap=None, isAccessibleForFree=None, maximumAttendeeCapacity=None, openingHoursSpecification=None, photo=None, publicAccess=None, smokingAllowed=None, specialOpeningHoursSpecification=None, currenciesAccepted=None, openingHours=None, paymentAccepted=None, priceRange=None):
        Organization.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, address, aggregateRating, alumni, areaServed, award, brand, contactPoint, department, dissolutionDate, duns, email, employee, event, faxNumber, founder, foundingDate, foundingLocation, funder, globalLocationNumber, hasOfferCatalog, hasPOS, isicV4, legalName, leiCode, location, logo, makesOffer, member, memberOf, naics, numberOfEmployees, owns, parentOrganization, publishingPrinciples, review, seeks, sponsor, subOrganization, taxID, telephone, vatID)
        Place.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, additionalProperty, address, aggregateRating, amenityFeature, branchCode, containedInPlace, containsPlace, event, faxNumber, geo, globalLocationNumber, hasMap, isAccessibleForFree, isicV4, logo, maximumAttendeeCapacity, openingHoursSpecification, photo, publicAccess, review, smokingAllowed, specialOpeningHoursSpecification, telephone)
        self.currenciesAccepted = currenciesAccepted
        self.openingHours = openingHours
        self.paymentAccepted = paymentAccepted
        self.priceRange = priceRange

    def set_currenciesAccepted(self, currenciesAccepted):
        self.currenciesAccepted = currenciesAccepted

    def get_currenciesAccepted(self):
        return self.currenciesAccepted

    def set_openingHours(self, openingHours):
        self.openingHours = openingHours

    def get_openingHours(self):
        return self.openingHours

    def set_paymentAccepted(self, paymentAccepted):
        self.paymentAccepted = paymentAccepted

    def get_paymentAccepted(self):
        return self.paymentAccepted

    def set_priceRange(self, priceRange):
        self.priceRange = priceRange

    def get_priceRange(self):
        return self.priceRange


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
