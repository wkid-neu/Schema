from PreprocessData.all_class_files.ListItem import ListItem
from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class HowToDirection(ListItem,CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, item=None, nextItem=None, position=None, previousItem=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, afterMedia=None, beforeMedia=None, duringMedia=None, performTime=None, prepTime=None, supply=None, tool=None, totalTime=None):
        ListItem.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, item, nextItem, position, previousItem)
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.afterMedia = afterMedia
        self.beforeMedia = beforeMedia
        self.duringMedia = duringMedia
        self.performTime = performTime
        self.prepTime = prepTime
        self.supply = supply
        self.tool = tool
        self.totalTime = totalTime

    def set_afterMedia(self, afterMedia):
        self.afterMedia = afterMedia

    def get_afterMedia(self):
        return self.afterMedia

    def set_beforeMedia(self, beforeMedia):
        self.beforeMedia = beforeMedia

    def get_beforeMedia(self):
        return self.beforeMedia

    def set_duringMedia(self, duringMedia):
        self.duringMedia = duringMedia

    def get_duringMedia(self):
        return self.duringMedia

    def set_performTime(self, performTime):
        self.performTime = performTime

    def get_performTime(self):
        return self.performTime

    def set_prepTime(self, prepTime):
        self.prepTime = prepTime

    def get_prepTime(self):
        return self.prepTime

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


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
