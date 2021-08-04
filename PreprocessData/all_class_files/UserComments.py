from PreprocessData.all_class_files.UserInteraction import UserInteraction
import global_data


class UserComments(UserInteraction):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, actor=None, aggregateRating=None, attendee=None, audience=None, composer=None, contributor=None, director=None, doorTime=None, duration=None, endDate=None, eventStatus=None, funder=None, inLanguage=None, isAccessibleForFree=None, location=None, maximumAttendeeCapacity=None, offers=None, organizer=None, performer=None, previousStartDate=None, recordedIn=None, remainingAttendeeCapacity=None, review=None, sponsor=None, startDate=None, subEvent=None, superEvent=None, translator=None, typicalAgeRange=None, workFeatured=None, workPerformed=None, commentText=None, commentTime=None, creator=None, discusses=None, replyToUrl=None):
        UserInteraction.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, actor, aggregateRating, attendee, audience, composer, contributor, director, doorTime, duration, endDate, eventStatus, funder, inLanguage, isAccessibleForFree, location, maximumAttendeeCapacity, offers, organizer, performer, previousStartDate, recordedIn, remainingAttendeeCapacity, review, sponsor, startDate, subEvent, superEvent, translator, typicalAgeRange, workFeatured, workPerformed)
        self.commentText = commentText
        self.commentTime = commentTime
        self.creator = creator
        self.discusses = discusses
        self.replyToUrl = replyToUrl

    def set_commentText(self, commentText):
        self.commentText = commentText

    def get_commentText(self):
        return self.commentText

    def set_commentTime(self, commentTime):
        self.commentTime = commentTime

    def get_commentTime(self):
        return self.commentTime

    def set_creator(self, creator):
        self.creator = creator

    def get_creator(self):
        return self.creator

    def set_discusses(self, discusses):
        self.discusses = discusses

    def get_discusses(self):
        return self.discusses

    def set_replyToUrl(self, replyToUrl):
        self.replyToUrl = replyToUrl

    def get_replyToUrl(self):
        return self.replyToUrl


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
