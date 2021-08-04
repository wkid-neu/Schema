from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class MusicComposition(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, composer=None, firstPerformance=None, includedComposition=None, iswcCode=None, lyricist=None, lyrics=None, musicArrangement=None, musicCompositionForm=None, musicalKey=None, recordedAs=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.composer = composer
        self.firstPerformance = firstPerformance
        self.includedComposition = includedComposition
        self.iswcCode = iswcCode
        self.lyricist = lyricist
        self.lyrics = lyrics
        self.musicArrangement = musicArrangement
        self.musicCompositionForm = musicCompositionForm
        self.musicalKey = musicalKey
        self.recordedAs = recordedAs

    def set_composer(self, composer):
        self.composer = composer

    def get_composer(self):
        return self.composer

    def set_firstPerformance(self, firstPerformance):
        self.firstPerformance = firstPerformance

    def get_firstPerformance(self):
        return self.firstPerformance

    def set_includedComposition(self, includedComposition):
        self.includedComposition = includedComposition

    def get_includedComposition(self):
        return self.includedComposition

    def set_iswcCode(self, iswcCode):
        self.iswcCode = iswcCode

    def get_iswcCode(self):
        return self.iswcCode

    def set_lyricist(self, lyricist):
        self.lyricist = lyricist

    def get_lyricist(self):
        return self.lyricist

    def set_lyrics(self, lyrics):
        self.lyrics = lyrics

    def get_lyrics(self):
        return self.lyrics

    def set_musicArrangement(self, musicArrangement):
        self.musicArrangement = musicArrangement

    def get_musicArrangement(self):
        return self.musicArrangement

    def set_musicCompositionForm(self, musicCompositionForm):
        self.musicCompositionForm = musicCompositionForm

    def get_musicCompositionForm(self):
        return self.musicCompositionForm

    def set_musicalKey(self, musicalKey):
        self.musicalKey = musicalKey

    def get_musicalKey(self):
        return self.musicalKey

    def set_recordedAs(self, recordedAs):
        self.recordedAs = recordedAs

    def get_recordedAs(self):
        return self.recordedAs


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
