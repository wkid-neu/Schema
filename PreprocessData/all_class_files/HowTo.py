from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class HowTo(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, estimatedCost=None, performTime=None, prepTime=None, step=None, supply=None, tool=None, totalTime=None, yielded=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.estimatedCost = estimatedCost
        self.performTime = performTime
        self.prepTime = prepTime
        self.step = step
        self.supply = supply
        self.tool = tool
        self.totalTime = totalTime
        self.yielded = yielded

    def set_estimatedCost(self, estimatedCost):
        self.estimatedCost = estimatedCost

    def get_estimatedCost(self):
        return self.estimatedCost

    def set_performTime(self, performTime):
        self.performTime = performTime

    def get_performTime(self):
        return self.performTime

    def set_prepTime(self, prepTime):
        self.prepTime = prepTime

    def get_prepTime(self):
        return self.prepTime

    def set_step(self, step):
        self.step = step

    def get_step(self):
        return self.step

    def set_supply(self, supply):
        self.supply = supply

    def get_supply(self):
        return self.supply

    def set_tool(self, tool):
        self.tool = tool

    def get_tool(self):
        return self.tool

    def set_totalTime(self, totalTime):
        self.totalTime = totalTime

    def get_totalTime(self):
        return self.totalTime

    def set_yielded(self, yielded):
        self.yielded = yielded

    def get_yielded(self):
        return self.yielded


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
