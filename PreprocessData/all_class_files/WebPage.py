from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class WebPage(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, breadcrumb=None, lastReviewed=None, mainContentOfPage=None, primaryImageOfPage=None, relatedLink=None, reviewedBy=None, significantLink=None, specialty=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.breadcrumb = breadcrumb
        self.lastReviewed = lastReviewed
        self.mainContentOfPage = mainContentOfPage
        self.primaryImageOfPage = primaryImageOfPage
        self.relatedLink = relatedLink
        self.reviewedBy = reviewedBy
        self.significantLink = significantLink
        self.specialty = specialty

    def set_breadcrumb(self, breadcrumb):
        self.breadcrumb = breadcrumb

    def get_breadcrumb(self):
        return self.breadcrumb

    def set_lastReviewed(self, lastReviewed):
        self.lastReviewed = lastReviewed

    def get_lastReviewed(self):
        return self.lastReviewed

    def set_mainContentOfPage(self, mainContentOfPage):
        self.mainContentOfPage = mainContentOfPage

    def get_mainContentOfPage(self):
        return self.mainContentOfPage

    def set_primaryImageOfPage(self, primaryImageOfPage):
        self.primaryImageOfPage = primaryImageOfPage

    def get_primaryImageOfPage(self):
        return self.primaryImageOfPage

    def set_relatedLink(self, relatedLink):
        self.relatedLink = relatedLink

    def get_relatedLink(self):
        return self.relatedLink

    def set_reviewedBy(self, reviewedBy):
        self.reviewedBy = reviewedBy

    def get_reviewedBy(self):
        return self.reviewedBy

    def set_significantLink(self, significantLink):
        self.significantLink = significantLink

    def get_significantLink(self):
        return self.significantLink

    def set_specialty(self, specialty):
        self.specialty = specialty

    def get_specialty(self):
        return self.specialty


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
