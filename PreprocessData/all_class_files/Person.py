from PreprocessData.all_class_files.Thing import Thing
import global_data


class Person(Thing):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalName=None, address=None, affiliation=None, alumniOf=None, award=None, birthDate=None, birthPlace=None, brand=None, children=None, colleague=None, contactPoint=None, deathDate=None, deathPlace=None, duns=None, email=None, familyName=None, faxNumber=None, follows=None, funder=None, gender=None, givenName=None, globalLocationNumber=None, hasOfferCatalog=None, hasPOS=None, height=None, homeLocation=None, honorificPrefix=None, honorificSuffix=None, isicV4=None, jobTitle=None, knows=None, makesOffer=None, memberOf=None, naics=None, nationality=None, netWorth=None, owns=None, parent=None, performerIn=None, publishingPrinciples=None, relatedTo=None, seeks=None, sibling=None, sponsor=None, spouse=None, taxID=None, telephone=None, vatID=None, weight=None, workLocation=None, worksFor=None):
        Thing.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.additionalName = additionalName
        self.address = address
        self.affiliation = affiliation
        self.alumniOf = alumniOf
        self.award = award
        self.birthDate = birthDate
        self.birthPlace = birthPlace
        self.brand = brand
        self.children = children
        self.colleague = colleague
        self.contactPoint = contactPoint
        self.deathDate = deathDate
        self.deathPlace = deathPlace
        self.duns = duns
        self.email = email
        self.familyName = familyName
        self.faxNumber = faxNumber
        self.follows = follows
        self.funder = funder
        self.gender = gender
        self.givenName = givenName
        self.globalLocationNumber = globalLocationNumber
        self.hasOfferCatalog = hasOfferCatalog
        self.hasPOS = hasPOS
        self.height = height
        self.homeLocation = homeLocation
        self.honorificPrefix = honorificPrefix
        self.honorificSuffix = honorificSuffix
        self.isicV4 = isicV4
        self.jobTitle = jobTitle
        self.knows = knows
        self.makesOffer = makesOffer
        self.memberOf = memberOf
        self.naics = naics
        self.nationality = nationality
        self.netWorth = netWorth
        self.owns = owns
        self.parent = parent
        self.performerIn = performerIn
        self.publishingPrinciples = publishingPrinciples
        self.relatedTo = relatedTo
        self.seeks = seeks
        self.sibling = sibling
        self.sponsor = sponsor
        self.spouse = spouse
        self.taxID = taxID
        self.telephone = telephone
        self.vatID = vatID
        self.weight = weight
        self.workLocation = workLocation
        self.worksFor = worksFor

    def set_additionalName(self, additionalName):
        self.additionalName = additionalName

    def get_additionalName(self):
        return self.additionalName

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_affiliation(self, affiliation):
        self.affiliation = affiliation

    def get_affiliation(self):
        return self.affiliation

    def set_alumniOf(self, alumniOf):
        self.alumniOf = alumniOf

    def get_alumniOf(self):
        return self.alumniOf

    def set_award(self, award):
        self.award = award

    def get_award(self):
        return self.award

    def set_birthDate(self, birthDate):
        self.birthDate = birthDate

    def get_birthDate(self):
        return self.birthDate

    def set_birthPlace(self, birthPlace):
        self.birthPlace = birthPlace

    def get_birthPlace(self):
        return self.birthPlace

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_children(self, children):
        self.children = children

    def get_children(self):
        return self.children

    def set_colleague(self, colleague):
        self.colleague = colleague

    def get_colleague(self):
        return self.colleague

    def set_contactPoint(self, contactPoint):
        self.contactPoint = contactPoint

    def get_contactPoint(self):
        return self.contactPoint

    def set_deathDate(self, deathDate):
        self.deathDate = deathDate

    def get_deathDate(self):
        return self.deathDate

    def set_deathPlace(self, deathPlace):
        self.deathPlace = deathPlace

    def get_deathPlace(self):
        return self.deathPlace

    def set_duns(self, duns):
        self.duns = duns

    def get_duns(self):
        return self.duns

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_familyName(self, familyName):
        self.familyName = familyName

    def get_familyName(self):
        return self.familyName

    def set_faxNumber(self, faxNumber):
        self.faxNumber = faxNumber

    def get_faxNumber(self):
        return self.faxNumber

    def set_follows(self, follows):
        self.follows = follows

    def get_follows(self):
        return self.follows

    def set_funder(self, funder):
        self.funder = funder

    def get_funder(self):
        return self.funder

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_givenName(self, givenName):
        self.givenName = givenName

    def get_givenName(self):
        return self.givenName

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

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_homeLocation(self, homeLocation):
        self.homeLocation = homeLocation

    def get_homeLocation(self):
        return self.homeLocation

    def set_honorificPrefix(self, honorificPrefix):
        self.honorificPrefix = honorificPrefix

    def get_honorificPrefix(self):
        return self.honorificPrefix

    def set_honorificSuffix(self, honorificSuffix):
        self.honorificSuffix = honorificSuffix

    def get_honorificSuffix(self):
        return self.honorificSuffix

    def set_isicV4(self, isicV4):
        self.isicV4 = isicV4

    def get_isicV4(self):
        return self.isicV4

    def set_jobTitle(self, jobTitle):
        self.jobTitle = jobTitle

    def get_jobTitle(self):
        return self.jobTitle

    def set_knows(self, knows):
        self.knows = knows

    def get_knows(self):
        return self.knows

    def set_makesOffer(self, makesOffer):
        self.makesOffer = makesOffer

    def get_makesOffer(self):
        return self.makesOffer

    def set_memberOf(self, memberOf):
        self.memberOf = memberOf

    def get_memberOf(self):
        return self.memberOf

    def set_naics(self, naics):
        self.naics = naics

    def get_naics(self):
        return self.naics

    def set_nationality(self, nationality):
        self.nationality = nationality

    def get_nationality(self):
        return self.nationality

    def set_netWorth(self, netWorth):
        self.netWorth = netWorth

    def get_netWorth(self):
        return self.netWorth

    def set_owns(self, owns):
        self.owns = owns

    def get_owns(self):
        return self.owns

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_performerIn(self, performerIn):
        self.performerIn = performerIn

    def get_performerIn(self):
        return self.performerIn

    def set_publishingPrinciples(self, publishingPrinciples):
        self.publishingPrinciples = publishingPrinciples

    def get_publishingPrinciples(self):
        return self.publishingPrinciples

    def set_relatedTo(self, relatedTo):
        self.relatedTo = relatedTo

    def get_relatedTo(self):
        return self.relatedTo

    def set_seeks(self, seeks):
        self.seeks = seeks

    def get_seeks(self):
        return self.seeks

    def set_sibling(self, sibling):
        self.sibling = sibling

    def get_sibling(self):
        return self.sibling

    def set_sponsor(self, sponsor):
        self.sponsor = sponsor

    def get_sponsor(self):
        return self.sponsor

    def set_spouse(self, spouse):
        self.spouse = spouse

    def get_spouse(self):
        return self.spouse

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

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_workLocation(self, workLocation):
        self.workLocation = workLocation

    def get_workLocation(self):
        return self.workLocation

    def set_worksFor(self, worksFor):
        self.worksFor = worksFor

    def get_worksFor(self):
        return self.worksFor


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
