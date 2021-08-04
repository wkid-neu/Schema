from PreprocessData.all_class_files.MediaObject import MediaObject
import global_data


class VideoObject(MediaObject):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, associatedArticle=None, bitrate=None, contentSize=None, contentUrl=None, duration=None, embedUrl=None, encodesCreativeWork=None, height=None, playerType=None, productionCompany=None, regionsAllowed=None, requiresSubscription=None, uploadDate=None, width=None, actor=None, caption=None, director=None, musicBy=None, thumbnail=None, transcript=None, videoFrameSize=None, videoQuality=None):
        MediaObject.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample, associatedArticle, bitrate, contentSize, contentUrl, duration, embedUrl, encodesCreativeWork, height, playerType, productionCompany, regionsAllowed, requiresSubscription, uploadDate, width)
        self.actor = actor
        self.caption = caption
        self.director = director
        self.musicBy = musicBy
        self.thumbnail = thumbnail
        self.transcript = transcript
        self.videoFrameSize = videoFrameSize
        self.videoQuality = videoQuality

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor

    def set_caption(self, caption):
        self.caption = caption

    def get_caption(self):
        return self.caption

    def set_director(self, director):
        self.director = director

    def get_director(self):
        return self.director

    def set_musicBy(self, musicBy):
        self.musicBy = musicBy

    def get_musicBy(self):
        return self.musicBy

    def set_thumbnail(self, thumbnail):
        self.thumbnail = thumbnail

    def get_thumbnail(self):
        return self.thumbnail

    def set_transcript(self, transcript):
        self.transcript = transcript

    def get_transcript(self):
        return self.transcript

    def set_videoFrameSize(self, videoFrameSize):
        self.videoFrameSize = videoFrameSize

    def get_videoFrameSize(self):
        return self.videoFrameSize

    def set_videoQuality(self, videoQuality):
        self.videoQuality = videoQuality

    def get_videoQuality(self):
        return self.videoQuality


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
