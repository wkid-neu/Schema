from PreprocessData.all_class_files.Thing import Thing
import global_data


class Event(Thing):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, actor=None, aggregateRating=None, attendee=None, audience=None, composer=None, contributor=None, director=None, doorTime=None, duration=None, endDate=None, eventStatus=None, funder=None, inLanguage=None, isAccessibleForFree=None, location=None, maximumAttendeeCapacity=None, offers=None, organizer=None, performer=None, previousStartDate=None, recordedIn=None, remainingAttendeeCapacity=None, review=None, sponsor=None, startDate=None, subEvent=None, superEvent=None, translator=None, typicalAgeRange=None, workFeatured=None, workPerformed=None):
        Thing.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.about = about
        self.actor = actor
        self.aggregateRating = aggregateRating
        self.attendee = attendee
        self.audience = audience
        self.composer = composer
        self.contributor = contributor
        self.director = director
        self.doorTime = doorTime
        self.duration = duration
        self.endDate = endDate
        self.eventStatus = eventStatus
        self.funder = funder
        self.inLanguage = inLanguage
        self.isAccessibleForFree = isAccessibleForFree
        self.location = location
        self.maximumAttendeeCapacity = maximumAttendeeCapacity
        self.offers = offers
        self.organizer = organizer
        self.performer = performer
        self.previousStartDate = previousStartDate
        self.recordedIn = recordedIn
        self.remainingAttendeeCapacity = remainingAttendeeCapacity
        self.review = review
        self.sponsor = sponsor
        self.startDate = startDate
        self.subEvent = subEvent
        self.superEvent = superEvent
        self.translator = translator
        self.typicalAgeRange = typicalAgeRange
        self.workFeatured = workFeatured
        self.workPerformed = workPerformed

    def set_about(self, about):
        self.about = about

    def get_about(self):
        return self.about

    def set_actor(self, actor):
        self.actor = actor

    def get_actor(self):
        return self.actor

    def set_aggregateRating(self, aggregateRating):
        self.aggregateRating = aggregateRating

    def get_aggregateRating(self):
        return self.aggregateRating

    def set_attendee(self, attendee):
        self.attendee = attendee

    def get_attendee(self):
        return self.attendee

    def set_audience(self, audience):
        self.audience = audience

    def get_audience(self):
        return self.audience

    def set_composer(self, composer):
        self.composer = composer

    def get_composer(self):
        return self.composer

    def set_contributor(self, contributor):
        self.contributor = contributor

    def get_contributor(self):
        return self.contributor

    def set_director(self, director):
        self.director = director

    def get_director(self):
        return self.director

    def set_doorTime(self, doorTime):
        self.doorTime = doorTime

    def get_doorTime(self):
        return self.doorTime

    def set_duration(self, duration):
        self.duration = duration

    def get_duration(self):
        return self.duration

    def set_endDate(self, endDate):
        self.endDate = endDate

    def get_endDate(self):
        return self.endDate

    def set_eventStatus(self, eventStatus):
        self.eventStatus = eventStatus

    def get_eventStatus(self):
        return self.eventStatus

    def set_funder(self, funder):
        self.funder = funder

    def get_funder(self):
        return self.funder

    def set_inLanguage(self, inLanguage):
        self.inLanguage = inLanguage

    def get_inLanguage(self):
        return self.inLanguage

    def set_isAccessibleForFree(self, isAccessibleForFree):
        self.isAccessibleForFree = isAccessibleForFree

    def get_isAccessibleForFree(self):
        return self.isAccessibleForFree

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_maximumAttendeeCapacity(self, maximumAttendeeCapacity):
        self.maximumAttendeeCapacity = maximumAttendeeCapacity

    def get_maximumAttendeeCapacity(self):
        return self.maximumAttendeeCapacity

    def set_offers(self, offers):
        self.offers = offers

    def get_offers(self):
        return self.offers

    def set_organizer(self, organizer):
        self.organizer = organizer

    def get_organizer(self):
        return self.organizer

    def set_performer(self, performer):
        self.performer = performer

    def get_performer(self):
        return self.performer

    def set_previousStartDate(self, previousStartDate):
        self.previousStartDate = previousStartDate

    def get_previousStartDate(self):
        return self.previousStartDate

    def set_recordedIn(self, recordedIn):
        self.recordedIn = recordedIn

    def get_recordedIn(self):
        return self.recordedIn

    def set_remainingAttendeeCapacity(self, remainingAttendeeCapacity):
        self.remainingAttendeeCapacity = remainingAttendeeCapacity

    def get_remainingAttendeeCapacity(self):
        return self.remainingAttendeeCapacity

    def set_review(self, review):
        self.review = review

    def get_review(self):
        return self.review

    def set_sponsor(self, sponsor):
        self.sponsor = sponsor

    def get_sponsor(self):
        return self.sponsor

    def set_startDate(self, startDate):
        self.startDate = startDate

    def get_startDate(self):
        return self.startDate

    def set_subEvent(self, subEvent):
        self.subEvent = subEvent

    def get_subEvent(self):
        return self.subEvent

    def set_superEvent(self, superEvent):
        self.superEvent = superEvent

    def get_superEvent(self):
        return self.superEvent

    def set_translator(self, translator):
        self.translator = translator

    def get_translator(self):
        return self.translator

    def set_typicalAgeRange(self, typicalAgeRange):
        self.typicalAgeRange = typicalAgeRange

    def get_typicalAgeRange(self):
        return self.typicalAgeRange

    def set_workFeatured(self, workFeatured):
        self.workFeatured = workFeatured

    def get_workFeatured(self):
        return self.workFeatured

    def set_workPerformed(self, workPerformed):
        self.workPerformed = workPerformed

    def get_workPerformed(self):
        return self.workPerformed


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
