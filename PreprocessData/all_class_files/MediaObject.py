from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class MediaObject(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, associatedArticle=None, bitrate=None, contentSize=None, contentUrl=None, duration=None, embedUrl=None, encodesCreativeWork=None, height=None, playerType=None, productionCompany=None, regionsAllowed=None, requiresSubscription=None, uploadDate=None, width=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.associatedArticle = associatedArticle
        self.bitrate = bitrate
        self.contentSize = contentSize
        self.contentUrl = contentUrl
        self.duration = duration
        self.embedUrl = embedUrl
        self.encodesCreativeWork = encodesCreativeWork
        self.encodingFormat = encodingFormat
        self.height = height
        self.playerType = playerType
        self.productionCompany = productionCompany
        self.regionsAllowed = regionsAllowed
        self.requiresSubscription = requiresSubscription
        self.uploadDate = uploadDate
        self.width = width

    def set_associatedArticle(self, associatedArticle):
        self.associatedArticle = associatedArticle

    def get_associatedArticle(self):
        return self.associatedArticle

    def set_bitrate(self, bitrate):
        self.bitrate = bitrate

    def get_bitrate(self):
        return self.bitrate

    def set_contentSize(self, contentSize):
        self.contentSize = contentSize

    def get_contentSize(self):
        return self.contentSize

    def set_contentUrl(self, contentUrl):
        self.contentUrl = contentUrl

    def get_contentUrl(self):
        return self.contentUrl

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def set_embedUrl(self, embedUrl):
        self.embedUrl = embedUrl

    def get_embedUrl(self):
        return self.embedUrl

    def set_encodesCreativeWork(self, encodesCreativeWork):
        self.encodesCreativeWork = encodesCreativeWork

    def get_encodesCreativeWork(self):
        return self.encodesCreativeWork

    def set_encodingFormat(self, encodingFormat):
        self.encodingFormat = encodingFormat

    def get_encodingFormat(self):
        return self.encodingFormat

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_playerType(self, playerType):
        self.playerType = playerType

    def get_playerType(self):
        return self.playerType

    def set_productionCompany(self, productionCompany):
        self.productionCompany = productionCompany

    def get_productionCompany(self):
        return self.productionCompany

    def set_regionsAllowed(self, regionsAllowed):
        self.regionsAllowed = regionsAllowed

    def get_regionsAllowed(self):
        return self.regionsAllowed

    def set_requiresSubscription(self, requiresSubscription):
        self.requiresSubscription = requiresSubscription

    def get_requiresSubscription(self):
        return self.requiresSubscription

    def set_uploadDate(self, uploadDate):
        self.uploadDate = uploadDate

    def get_uploadDate(self):
        return self.uploadDate

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
