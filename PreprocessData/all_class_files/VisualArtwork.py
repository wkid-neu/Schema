from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class VisualArtwork(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, artEdition=None, artMedium=None, artform=None, artworkSurface=None, depth=None, height=None, width=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.artEdition = artEdition
        self.artMedium = artMedium
        self.artform = artform
        self.artworkSurface = artworkSurface
        self.depth = depth
        self.height = height
        self.width = width

    def set_artEdition(self, artEdition):
        self.artEdition = artEdition

    def get_artEdition(self):
        return self.artEdition

    def set_artMedium(self, artMedium):
        self.artMedium = artMedium

    def get_artMedium(self):
        return self.artMedium

    def set_artform(self, artform):
        self.artform = artform

    def get_artform(self):
        return self.artform

    def set_artworkSurface(self, artworkSurface):
        self.artworkSurface = artworkSurface

    def get_artworkSurface(self):
        return self.artworkSurface

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
