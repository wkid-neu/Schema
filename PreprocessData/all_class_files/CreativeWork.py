from PreprocessData.all_class_files.Thing import Thing
import global_data


class CreativeWork(Thing):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None):
        Thing.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.about = about
        self.accessMode = accessMode
        self.accessModeSufficient = accessModeSufficient
        self.accessibilityAPI = accessibilityAPI
        self.accessibilityControl = accessibilityControl
        self.accessibilityFeature = accessibilityFeature
        self.accessibilityHazard = accessibilityHazard
        self.accessibilitySummary = accessibilitySummary
        self.accountablePerson = accountablePerson
        self.aggregateRating = aggregateRating
        self.alternativeHeadline = alternativeHeadline
        self.associatedMedia = associatedMedia
        self.audience = audience
        self.audio = audio
        self.author = author
        self.award = award
        self.character = character
        self.citation = citation
        self.comment = comment
        self.commentCount = commentCount
        self.contentLocation = contentLocation
        self.contentRating = contentRating
        self.contributor = contributor
        self.copyrightHolder = copyrightHolder
        self.copyrightYear = copyrightYear
        self.creator = creator
        self.dateCreated = dateCreated
        self.dateModified = dateModified
        self.datePublished = datePublished
        self.discussionUrl = discussionUrl
        self.editor = editor
        self.educationalAlignment = educationalAlignment
        self.educationalUse = educationalUse
        self.encoding = encoding
        self.encodingFormat = encodingFormat
        self.exampleOfWork = exampleOfWork
        self.expires = expires
        self.funder = funder
        self.genre = genre
        self.hasPart = hasPart
        self.headline = headline
        self.inLanguage = inLanguage
        self.interactionStatistic = interactionStatistic
        self.interactivityType = interactivityType
        self.isAccessibleForFree = isAccessibleForFree
        self.isBasedOn = isBasedOn
        self.isFamilyFriendly = isFamilyFriendly
        self.isPartOf = isPartOf
        self.keywords = keywords
        self.learningResourceType = learningResourceType
        self.license = license
        self.locationCreated = locationCreated
        self.mainEntity = mainEntity
        self.material = material
        self.mentions = mentions
        self.offers = offers
        self.position = position
        self.producer = producer
        self.provider = provider
        self.publication = publication
        self.publisher = publisher
        self.publishingPrinciples = publishingPrinciples
        self.recordedAt = recordedAt
        self.releasedEvent = releasedEvent
        self.review = review
        self.schemaVersion = schemaVersion
        self.sourceOrganization = sourceOrganization
        self.spatialCoverage = spatialCoverage
        self.sponsor = sponsor
        self.temporalCoverage = temporalCoverage
        self.text = text
        self.thumbnailUrl = thumbnailUrl
        self.timeRequired = timeRequired
        self.translator = translator
        self.typicalAgeRange = typicalAgeRange
        self.version = version
        self.video = video
        self.workExample = workExample

    def set_about(self, about):
        self.about = about

    def get_about(self):
        return self.about

    def set_accessMode(self, accessMode):
        self.accessMode = accessMode

    def get_accessMode(self):
        return self.accessMode

    def set_accessModeSufficient(self, accessModeSufficient):
        self.accessModeSufficient = accessModeSufficient

    def get_accessModeSufficient(self):
        return self.accessModeSufficient

    def set_accessibilityAPI(self, accessibilityAPI):
        self.accessibilityAPI = accessibilityAPI

    def get_accessibilityAPI(self):
        return self.accessibilityAPI

    def set_accessibilityControl(self, accessibilityControl):
        self.accessibilityControl = accessibilityControl

    def get_accessibilityControl(self):
        return self.accessibilityControl

    def set_accessibilityFeature(self, accessibilityFeature):
        self.accessibilityFeature = accessibilityFeature

    def get_accessibilityFeature(self):
        return self.accessibilityFeature

    def set_accessibilityHazard(self, accessibilityHazard):
        self.accessibilityHazard = accessibilityHazard

    def get_accessibilityHazard(self):
        return self.accessibilityHazard

    def set_accessibilitySummary(self, accessibilitySummary):
        self.accessibilitySummary = accessibilitySummary

    def get_accessibilitySummary(self):
        return self.accessibilitySummary

    def set_accountablePerson(self, accountablePerson):
        self.accountablePerson = accountablePerson

    def get_accountablePerson(self):
        return self.accountablePerson

    def set_aggregateRating(self, aggregateRating):
        self.aggregateRating = aggregateRating

    def get_aggregateRating(self):
        return self.aggregateRating

    def set_alternativeHeadline(self, alternativeHeadline):
        self.alternativeHeadline = alternativeHeadline

    def get_alternativeHeadline(self):
        return self.alternativeHeadline

    def set_associatedMedia(self, associatedMedia):
        self.associatedMedia = associatedMedia

    def get_associatedMedia(self):
        return self.associatedMedia

    def set_audience(self, audience):
        self.audience = audience

    def get_audience(self):
        return self.audience

    def set_audio(self, audio):
        self.audio = audio

    def get_audio(self):
        return self.audio

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_award(self, award):
        self.award = award

    def get_award(self):
        return self.award

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_citation(self, citation):
        self.citation = citation

    def get_citation(self):
        return self.citation

    def set_comment(self, comment):
        self.comment = comment

    def get_comment(self):
        return self.comment

    def set_commentCount(self, commentCount):
        self.commentCount = commentCount

    def get_commentCount(self):
        return self.commentCount

    def set_contentLocation(self, contentLocation):
        self.contentLocation = contentLocation

    def get_contentLocation(self):
        return self.contentLocation

    def set_contentRating(self, contentRating):
        self.contentRating = contentRating

    def get_contentRating(self):
        return self.contentRating

    def set_contributor(self, contributor):
        self.contributor = contributor

    def get_contributor(self):
        return self.contributor

    def set_copyrightHolder(self, copyrightHolder):
        self.copyrightHolder = copyrightHolder

    def get_copyrightHolder(self):
        return self.copyrightHolder

    def set_copyrightYear(self, copyrightYear):
        self.copyrightYear = copyrightYear

    def get_copyrightYear(self):
        return self.copyrightYear

    def set_creator(self, creator):
        self.creator = creator

    def get_creator(self):
        return self.creator

    def set_dateCreated(self, dateCreated):
        self.dateCreated = dateCreated

    def get_dateCreated(self):
        return self.dateCreated

    def set_dateModified(self, dateModified):
        self.dateModified = dateModified

    def get_dateModified(self):
        return self.dateModified

    def set_datePublished(self, datePublished):
        self.datePublished = datePublished

    def get_datePublished(self):
        return self.datePublished

    def set_discussionUrl(self, discussionUrl):
        self.discussionUrl = discussionUrl

    def get_discussionUrl(self):
        return self.discussionUrl

    def set_editor(self, editor):
        self.editor = editor

    def get_editor(self):
        return self.editor

    def set_educationalAlignment(self, educationalAlignment):
        self.educationalAlignment = educationalAlignment

    def get_educationalAlignment(self):
        return self.educationalAlignment

    def set_educationalUse(self, educationalUse):
        self.educationalUse = educationalUse

    def get_educationalUse(self):
        return self.educationalUse

    def set_encoding(self, encoding):
        self.encoding = encoding

    def get_encoding(self):
        return self.encoding

    def set_encodingFormat(self, encodingFormat):
        self.encodingFormat = encodingFormat

    def get_encodingFormat(self):
        return self.encodingFormat

    def set_exampleOfWork(self, exampleOfWork):
        self.exampleOfWork = exampleOfWork

    def get_exampleOfWork(self):
        return self.exampleOfWork

    def set_expires(self, expires):
        self.expires = expires

    def get_expires(self):
        return self.expires

    def set_funder(self, funder):
        self.funder = funder

    def get_funder(self):
        return self.funder

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_hasPart(self, hasPart):
        self.hasPart = hasPart

    def get_hasPart(self):
        return self.hasPart

    def set_headline(self, headline):
        self.headline = headline

    def get_headline(self):
        return self.headline

    def set_inLanguage(self, inLanguage):
        self.inLanguage = inLanguage

    def get_inLanguage(self):
        return self.inLanguage

    def set_interactionStatistic(self, interactionStatistic):
        self.interactionStatistic = interactionStatistic

    def get_interactionStatistic(self):
        return self.interactionStatistic

    def set_interactivityType(self, interactivityType):
        self.interactivityType = interactivityType

    def get_interactivityType(self):
        return self.interactivityType

    def set_isAccessibleForFree(self, isAccessibleForFree):
        self.isAccessibleForFree = isAccessibleForFree

    def get_isAccessibleForFree(self):
        return self.isAccessibleForFree

    def set_isBasedOn(self, isBasedOn):
        self.isBasedOn = isBasedOn

    def get_isBasedOn(self):
        return self.isBasedOn

    def set_isFamilyFriendly(self, isFamilyFriendly):
        self.isFamilyFriendly = isFamilyFriendly

    def get_isFamilyFriendly(self):
        return self.isFamilyFriendly

    def set_isPartOf(self, isPartOf):
        self.isPartOf = isPartOf

    def get_isPartOf(self):
        return self.isPartOf

    def set_keywords(self, keywords):
        self.keywords = keywords

    def get_keywords(self):
        return self.keywords

    def set_learningResourceType(self, learningResourceType):
        self.learningResourceType = learningResourceType

    def get_learningResourceType(self):
        return self.learningResourceType

    def set_license(self, license):
        self.license = license

    def get_license(self):
        return self.license

    def set_locationCreated(self, locationCreated):
        self.locationCreated = locationCreated

    def get_locationCreated(self):
        return self.locationCreated

    def set_mainEntity(self, mainEntity):
        self.mainEntity = mainEntity

    def get_mainEntity(self):
        return self.mainEntity

    def set_material(self, material):
        self.material = material

    def get_material(self):
        return self.material

    def set_mentions(self, mentions):
        self.mentions = mentions

    def get_mentions(self):
        return self.mentions

    def set_offers(self, offers):
        self.offers = offers

    def get_offers(self):
        return self.offers

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def set_producer(self, producer):
        self.producer = producer

    def get_producer(self):
        return self.producer

    def set_provider(self, provider):
        self.provider = provider

    def get_provider(self):
        return self.provider

    def set_publication(self, publication):
        self.publication = publication

    def get_publication(self):
        return self.publication

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_publishingPrinciples(self, publishingPrinciples):
        self.publishingPrinciples = publishingPrinciples

    def get_publishingPrinciples(self):
        return self.publishingPrinciples

    def set_recordedAt(self, recordedAt):
        self.recordedAt = recordedAt

    def get_recordedAt(self):
        return self.recordedAt

    def set_releasedEvent(self, releasedEvent):
        self.releasedEvent = releasedEvent

    def get_releasedEvent(self):
        return self.releasedEvent

    def set_review(self, review):
        self.review = review

    def get_review(self):
        return self.review

    def set_schemaVersion(self, schemaVersion):
        self.schemaVersion = schemaVersion

    def get_schemaVersion(self):
        return self.schemaVersion

    def set_sourceOrganization(self, sourceOrganization):
        self.sourceOrganization = sourceOrganization

    def get_sourceOrganization(self):
        return self.sourceOrganization

    def set_spatialCoverage(self, spatialCoverage):
        self.spatialCoverage = spatialCoverage

    def get_spatialCoverage(self):
        return self.spatialCoverage

    def set_sponsor(self, sponsor):
        self.sponsor = sponsor

    def get_sponsor(self):
        return self.sponsor

    def set_temporalCoverage(self, temporalCoverage):
        self.temporalCoverage = temporalCoverage

    def get_temporalCoverage(self):
        return self.temporalCoverage

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def set_thumbnailUrl(self, thumbnailUrl):
        self.thumbnailUrl = thumbnailUrl

    def get_thumbnailUrl(self):
        return self.thumbnailUrl

    def set_timeRequired(self, timeRequired):
        self.timeRequired = timeRequired

    def get_timeRequired(self):
        return self.timeRequired

    def set_translator(self, translator):
        self.translator = translator

    def get_translator(self):
        return self.translator

    def set_typicalAgeRange(self, typicalAgeRange):
        self.typicalAgeRange = typicalAgeRange

    def get_typicalAgeRange(self):
        return self.typicalAgeRange

    def set_version(self, version):
        self.version = version

    def get_version(self):
        return self.version

    def set_video(self, video):
        self.video = video

    def get_video(self):
        return self.video

    def set_workExample(self, workExample):
        self.workExample = workExample

    def get_workExample(self):
        return self.workExample


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
