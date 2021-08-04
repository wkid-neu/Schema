from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class Message(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, bccRecipient=None, ccRecipient=None, dateRead=None, dateReceived=None, dateSent=None, messageAttachment=None, recipient=None, sender=None, toRecipient=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.bccRecipient = bccRecipient
        self.ccRecipient = ccRecipient
        self.dateRead = dateRead
        self.dateReceived = dateReceived
        self.dateSent = dateSent
        self.messageAttachment = messageAttachment
        self.recipient = recipient
        self.sender = sender
        self.toRecipient = toRecipient

    def set_bccRecipient(self, bccRecipient):
        self.bccRecipient = bccRecipient

    def get_bccRecipient(self):
        return self.bccRecipient

    def set_ccRecipient(self, ccRecipient):
        self.ccRecipient = ccRecipient

    def get_ccRecipient(self):
        return self.ccRecipient

    def set_dateRead(self, dateRead):
        self.dateRead = dateRead

    def get_dateRead(self):
        return self.dateRead

    def set_dateReceived(self, dateReceived):
        self.dateReceived = dateReceived

    def get_dateReceived(self):
        return self.dateReceived

    def set_dateSent(self, dateSent):
        self.dateSent = dateSent

    def get_dateSent(self):
        return self.dateSent

    def set_messageAttachment(self, messageAttachment):
        self.messageAttachment = messageAttachment

    def get_messageAttachment(self):
        return self.messageAttachment

    def set_recipient(self, recipient):
        self.recipient = recipient

    def get_recipient(self):
        return self.recipient

    def set_sender(self, sender):
        self.sender = sender

    def get_sender(self):
        return self.sender

    def set_toRecipient(self, toRecipient):
        self.toRecipient = toRecipient

    def get_toRecipient(self):
        return self.toRecipient


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
