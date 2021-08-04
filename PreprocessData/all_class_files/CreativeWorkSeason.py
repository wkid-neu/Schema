from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class CreativeWorkSeason(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, actor=None, director=None, endDate=None, episode=None, numberOfEpisodes=None, partOfSeries=None, productionCompany=None, seasonNumber=None, startDate=None, trailer=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.actor = actor
        self.director = director
        self.endDate = endDate
        self.episode = episode
        self.numberOfEpisodes = numberOfEpisodes
        self.partOfSeries = partOfSeries
        self.productionCompany = productionCompany
        self.seasonNumber = seasonNumber
        self.startDate = startDate
        self.trailer = trailer

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor

    def set_director(self, director):
        self.director = director

    def get_director(self):
        return self.director

    def set_endDate(self, endDate):
        self.endDate = endDate

    def get_endDate(self):
        return self.endDate

    def set_episode(self, episode):
        self.episode = episode

    def get_episode(self):
        return self.episode

    def set_numberOfEpisodes(self, numberOfEpisodes):
        self.numberOfEpisodes = numberOfEpisodes

    def get_numberOfEpisodes(self):
        return self.numberOfEpisodes

    def set_partOfSeries(self, partOfSeries):
        self.partOfSeries = partOfSeries

    def get_partOfSeries(self):
        return self.partOfSeries

    def set_productionCompany(self, productionCompany):
        self.productionCompany = productionCompany

    def get_productionCompany(self):
        return self.productionCompany

    def set_seasonNumber(self, seasonNumber):
        self.seasonNumber = seasonNumber

    def get_seasonNumber(self):
        return self.seasonNumber

    def set_startDate(self, startDate):
        self.startDate = startDate

    def get_startDate(self):
        return self.startDate

    def set_trailer(self, trailer):
        self.trailer = trailer

    def get_trailer(self):
        return self.trailer


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
