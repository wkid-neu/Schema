from PreprocessData.all_class_files.Thing import Thing
import global_data


class Organization(Thing):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, address=None, aggregateRating=None, alumni=None, areaServed=None, award=None, brand=None, contactPoint=None, department=None, dissolutionDate=None, duns=None, email=None, employee=None, event=None, faxNumber=None, founder=None, foundingDate=None, foundingLocation=None, funder=None, globalLocationNumber=None, hasOfferCatalog=None, hasPOS=None, isicV4=None, legalName=None, leiCode=None, location=None, logo=None, makesOffer=None, member=None, memberOf=None, naics=None, numberOfEmployees=None, owns=None, parentOrganization=None, publishingPrinciples=None, review=None, seeks=None, sponsor=None, subOrganization=None, taxID=None, telephone=None, vatID=None):
        Thing.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.address = address
        self.aggregateRating = aggregateRating
        self.alumni = alumni
        self.areaServed = areaServed
        self.award = award
        self.brand = brand
        self.contactPoint = contactPoint
        self.department = department
        self.dissolutionDate = dissolutionDate
        self.duns = duns
        self.email = email
        self.employee = employee
        self.event = event
        self.faxNumber = faxNumber
        self.founder = founder
        self.foundingDate = foundingDate
        self.foundingLocation = foundingLocation
        self.funder = funder
        self.globalLocationNumber = globalLocationNumber
        self.hasOfferCatalog = hasOfferCatalog
        self.hasPOS = hasPOS
        self.isicV4 = isicV4
        self.legalName = legalName
        self.leiCode = leiCode
        self.location = location
        self.logo = logo
        self.makesOffer = makesOffer
        self.member = member
        self.memberOf = memberOf
        self.naics = naics
        self.numberOfEmployees = numberOfEmployees
        self.owns = owns
        self.parentOrganization = parentOrganization
        self.publishingPrinciples = publishingPrinciples
        self.review = review
        self.seeks = seeks
        self.sponsor = sponsor
        self.subOrganization = subOrganization
        self.taxID = taxID
        self.telephone = telephone
        self.vatID = vatID

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_aggregateRating(self, aggregateRating):
        self.aggregateRating = aggregateRating

    def get_aggregateRating(self):
        return self.aggregateRating

    def set_alumni(self, alumni):
        self.alumni = alumni

    def get_alumni(self):
        return self.alumni

    def set_areaServed(self, areaServed):
        self.areaServed = areaServed

    def get_areaServed(self):
        return self.areaServed

    def set_award(self, award):
        self.award = award

    def get_award(self):
        return self.award

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_contactPoint(self, contactPoint):
        self.contactPoint = contactPoint

    def get_contactPoint(self):
        return self.contactPoint

    def set_department(self, department):
        self.department = department

    def get_department(self):
        return self.department

    def set_dissolutionDate(self, dissolutionDate):
        self.dissolutionDate = dissolutionDate

    def get_dissolutionDate(self):
        return self.dissolutionDate

    def set_duns(self, duns):
        self.duns = duns

    def get_duns(self):
        return self.duns

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_employee(self, employee):
        self.employee = employee

    def get_employee(self):
        return self.employee

    def set_event(self, event):
        self.event = event

    def get_event(self):
        return self.event

    def set_faxNumber(self, faxNumber):
        self.faxNumber = faxNumber

    def get_faxNumber(self):
        return self.faxNumber

    def set_founder(self, founder):
        self.founder = founder

    def get_founder(self):
        return self.founder

    def set_foundingDate(self, foundingDate):
        self.foundingDate = foundingDate

    def get_foundingDate(self):
        return self.foundingDate

    def set_foundingLocation(self, foundingLocation):
        self.foundingLocation = foundingLocation

    def get_foundingLocation(self):
        return self.foundingLocation

    def set_funder(self, funder):
        self.funder = funder

    def get_funder(self):
        return self.funder

    def set_globalLocationNumber(self, globalLocationNumber):
        self.globalLocationNumber = globalLocationNumber

    def get_globalLocationNumber(self):
        return self.globalLocationNumber

    def set_hasOfferCatalog(self, hasOfferCatalog):
        self.hasOfferCatalog = hasOfferCatalog

    def get_hasOfferCatalog(self):
        return self.hasOfferCatalog

    def set_hasPOS(self, hasPOS):
        self.hasPOS = hasPOS

    def get_hasPOS(self):
        return self.hasPOS

    def set_isicV4(self, isicV4):
        self.isicV4 = isicV4

    def get_isicV4(self):
        return self.isicV4

    def set_legalName(self, legalName):
        self.legalName = legalName

    def get_legalName(self):
        return self.legalName

    def set_leiCode(self, leiCode):
        self.leiCode = leiCode

    def get_leiCode(self):
        return self.leiCode

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_logo(self, logo):
        self.logo = logo

    def get_logo(self):
        return self.logo

    def set_makesOffer(self, makesOffer):
        self.makesOffer = makesOffer

    def get_makesOffer(self):
        return self.makesOffer

    def set_member(self, member):
        self.member = member

    def get_member(self):
        return self.member

    def set_memberOf(self, memberOf):
        self.memberOf = memberOf

    def get_memberOf(self):
        return self.memberOf

    def set_naics(self, naics):
        self.naics = naics

    def get_naics(self):
        return self.naics

    def set_numberOfEmployees(self, numberOfEmployees):
        self.numberOfEmployees = numberOfEmployees

    def get_numberOfEmployees(self):
        return self.numberOfEmployees

    def set_owns(self, owns):
        self.owns = owns

    def get_owns(self):
        return self.owns

    def set_parentOrganization(self, parentOrganization):
        self.parentOrganization = parentOrganization

    def get_parentOrganization(self):
        return self.parentOrganization

    def set_publishingPrinciples(self, publishingPrinciples):
        self.publishingPrinciples = publishingPrinciples

    def get_publishingPrinciples(self):
        return self.publishingPrinciples

    def set_review(self, review):
        self.review = review

    def get_review(self):
        return self.review

    def set_seeks(self, seeks):
        self.seeks = seeks

    def get_seeks(self):
        return self.seeks

    def set_sponsor(self, sponsor):
        self.sponsor = sponsor

    def get_sponsor(self):
        return self.sponsor

    def set_subOrganization(self, subOrganization):
        self.subOrganization = subOrganization

    def get_subOrganization(self):
        return self.subOrganization

    def set_taxID(self, taxID):
        self.taxID = taxID

    def get_taxID(self):
        return self.taxID

    def set_telephone(self, telephone):
        self.telephone = telephone

    def get_telephone(self):
        return self.telephone

    def set_vatID(self, vatID):
        self.vatID = vatID

    def get_vatID(self):
        return self.vatID


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
