from PreprocessData.all_class_files.CreativeWorkSeries import CreativeWorkSeries
import global_data


class RadioSeries(CreativeWorkSeries):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, endDate=None, issn=None, startDate=None, actor=None, containsSeason=None, director=None, episode=None, musicBy=None, numberOfEpisodes=None, numberOfSeasons=None, productionCompany=None, trailer=None):
        CreativeWorkSeries.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample, endDate, issn, startDate)
        self.actor = actor
        self.containsSeason = containsSeason
        self.director = director
        self.episode = episode
        self.musicBy = musicBy
        self.numberOfEpisodes = numberOfEpisodes
        self.numberOfSeasons = numberOfSeasons
        self.productionCompany = productionCompany
        self.trailer = trailer

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor

    def set_containsSeason(self, containsSeason):
        self.containsSeason = containsSeason

    def get_containsSeason(self):
        return self.containsSeason

    def set_director(self, director):
        self.director = director

    def get_director(self):
        return self.director

    def set_episode(self, episode):
        self.episode = episode

    def get_episode(self):
        return self.episode

    def set_musicBy(self, musicBy):
        self.musicBy = musicBy

    def get_musicBy(self):
        return self.musicBy

    def set_numberOfEpisodes(self, numberOfEpisodes):
        self.numberOfEpisodes = numberOfEpisodes

    def get_numberOfEpisodes(self):
        return self.numberOfEpisodes

    def set_numberOfSeasons(self, numberOfSeasons):
        self.numberOfSeasons = numberOfSeasons

    def get_numberOfSeasons(self):
        return self.numberOfSeasons

    def set_productionCompany(self, productionCompany):
        self.productionCompany = productionCompany

    def get_productionCompany(self):
        return self.productionCompany

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
