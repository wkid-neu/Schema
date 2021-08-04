from PreprocessData.all_class_files.PerformingGroup import PerformingGroup
import global_data


class MusicGroup(PerformingGroup):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, address=None, aggregateRating=None, alumni=None, areaServed=None, award=None, brand=None, contactPoint=None, department=None, dissolutionDate=None, duns=None, email=None, employee=None, event=None, faxNumber=None, founder=None, foundingDate=None, foundingLocation=None, funder=None, globalLocationNumber=None, hasOfferCatalog=None, hasPOS=None, isicV4=None, legalName=None, leiCode=None, location=None, logo=None, makesOffer=None, member=None, memberOf=None, naics=None, numberOfEmployees=None, owns=None, parentOrganization=None, publishingPrinciples=None, review=None, seeks=None, sponsor=None, subOrganization=None, taxID=None, telephone=None, vatID=None, album=None, genre=None, track=None):
        PerformingGroup.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, address, aggregateRating, alumni, areaServed, award, brand, contactPoint, department, dissolutionDate, duns, email, employee, event, faxNumber, founder, foundingDate, foundingLocation, funder, globalLocationNumber, hasOfferCatalog, hasPOS, isicV4, legalName, leiCode, location, logo, makesOffer, member, memberOf, naics, numberOfEmployees, owns, parentOrganization, publishingPrinciples, review, seeks, sponsor, subOrganization, taxID, telephone, vatID)
        self.album = album
        self.genre = genre
        self.track = track

    def set_album(self, album):
        self.album = album

    def get_album(self):
        return self.album

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_track(self, track):
        self.track = track

    def get_track(self):
        return self.track


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
