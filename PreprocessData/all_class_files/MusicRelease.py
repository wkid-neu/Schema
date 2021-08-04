from PreprocessData.all_class_files.MusicPlaylist import MusicPlaylist
import global_data


class MusicRelease(MusicPlaylist):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, numTracks=None, track=None, catalogNumber=None, creditedTo=None, duration=None, musicReleaseFormat=None, recordLabel=None, releaseOf=None):
        MusicPlaylist.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample, numTracks, track)
        self.catalogNumber = catalogNumber
        self.creditedTo = creditedTo
        self.duration = duration
        self.musicReleaseFormat = musicReleaseFormat
        self.recordLabel = recordLabel
        self.releaseOf = releaseOf

    def set_catalogNumber(self, catalogNumber):
        self.catalogNumber = catalogNumber

    def get_catalogNumber(self):
        return self.catalogNumber

    def set_creditedTo(self, creditedTo):
        self.creditedTo = creditedTo

    def get_creditedTo(self):
        return self.creditedTo

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def set_musicReleaseFormat(self, musicReleaseFormat):
        self.musicReleaseFormat = musicReleaseFormat

    def get_musicReleaseFormat(self):
        return self.musicReleaseFormat

    def set_recordLabel(self, recordLabel):
        self.recordLabel = recordLabel

    def get_recordLabel(self):
        return self.recordLabel

    def set_releaseOf(self, releaseOf):
        self.releaseOf = releaseOf

    def get_releaseOf(self):
        return self.releaseOf


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
