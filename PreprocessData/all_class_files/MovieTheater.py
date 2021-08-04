from PreprocessData.all_class_files.CivicStructure import CivicStructure
from PreprocessData.all_class_files.EntertainmentBusiness import EntertainmentBusiness
import global_data


class MovieTheater(CivicStructure,EntertainmentBusiness):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalProperty=None, address=None, aggregateRating=None, amenityFeature=None, branchCode=None, containedInPlace=None, containsPlace=None, event=None, faxNumber=None, geo=None, globalLocationNumber=None, hasMap=None, isAccessibleForFree=None, isicV4=None, logo=None, maximumAttendeeCapacity=None, openingHoursSpecification=None, photo=None, publicAccess=None, review=None, smokingAllowed=None, specialOpeningHoursSpecification=None, telephone=None, openingHours=None, alumni=None, areaServed=None, award=None, brand=None, contactPoint=None, department=None, dissolutionDate=None, duns=None, email=None, employee=None, founder=None, foundingDate=None, foundingLocation=None, funder=None, hasOfferCatalog=None, hasPOS=None, legalName=None, leiCode=None, location=None, makesOffer=None, member=None, memberOf=None, naics=None, numberOfEmployees=None, owns=None, parentOrganization=None, publishingPrinciples=None, seeks=None, sponsor=None, subOrganization=None, taxID=None, vatID=None, currenciesAccepted=None, paymentAccepted=None, priceRange=None, screenCount=None):
        CivicStructure.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, additionalProperty, address, aggregateRating, amenityFeature, branchCode, containedInPlace, containsPlace, event, faxNumber, geo, globalLocationNumber, hasMap, isAccessibleForFree, isicV4, logo, maximumAttendeeCapacity, openingHoursSpecification, photo, publicAccess, review, smokingAllowed, specialOpeningHoursSpecification, telephone, openingHours)
        EntertainmentBusiness.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, address, aggregateRating, alumni, areaServed, award, brand, contactPoint, department, dissolutionDate, duns, email, employee, event, faxNumber, founder, foundingDate, foundingLocation, funder, globalLocationNumber, hasOfferCatalog, hasPOS, isicV4, legalName, leiCode, location, logo, makesOffer, member, memberOf, naics, numberOfEmployees, owns, parentOrganization, publishingPrinciples, review, seeks, sponsor, subOrganization, taxID, telephone, vatID, additionalProperty, amenityFeature, branchCode, containedInPlace, containsPlace, geo, hasMap, isAccessibleForFree, maximumAttendeeCapacity, openingHoursSpecification, photo, publicAccess, smokingAllowed, specialOpeningHoursSpecification, currenciesAccepted, openingHours, paymentAccepted, priceRange)
        self.screenCount = screenCount

    def set_screenCount(self, screenCount):
        self.screenCount = screenCount

    def get_screenCount(self):
        return self.screenCount


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
