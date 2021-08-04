from PreprocessData.all_class_files.CreativeWork import CreativeWork
import global_data


class SoftwareApplication(CreativeWork):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, applicationCategory=None, applicationSubCategory=None, applicationSuite=None, availableOnDevice=None, countriesNotSupported=None, countriesSupported=None, downloadUrl=None, featureList=None, fileSize=None, installUrl=None, memoryRequirements=None, operatingSystem=None, permissions=None, processorRequirements=None, releaseNotes=None, screenshot=None, softwareAddOn=None, softwareHelp=None, softwareRequirements=None, softwareVersion=None, storageRequirements=None, supportingData=None):
        CreativeWork.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample)
        self.applicationCategory = applicationCategory
        self.applicationSubCategory = applicationSubCategory
        self.applicationSuite = applicationSuite
        self.availableOnDevice = availableOnDevice
        self.countriesNotSupported = countriesNotSupported
        self.countriesSupported = countriesSupported
        self.downloadUrl = downloadUrl
        self.featureList = featureList
        self.fileSize = fileSize
        self.installUrl = installUrl
        self.memoryRequirements = memoryRequirements
        self.operatingSystem = operatingSystem
        self.permissions = permissions
        self.processorRequirements = processorRequirements
        self.releaseNotes = releaseNotes
        self.screenshot = screenshot
        self.softwareAddOn = softwareAddOn
        self.softwareHelp = softwareHelp
        self.softwareRequirements = softwareRequirements
        self.softwareVersion = softwareVersion
        self.storageRequirements = storageRequirements
        self.supportingData = supportingData

    def set_applicationCategory(self, applicationCategory):
        self.applicationCategory = applicationCategory

    def get_applicationCategory(self):
        return self.applicationCategory

    def set_applicationSubCategory(self, applicationSubCategory):
        self.applicationSubCategory = applicationSubCategory

    def get_applicationSubCategory(self):
        return self.applicationSubCategory

    def set_applicationSuite(self, applicationSuite):
        self.applicationSuite = applicationSuite

    def get_applicationSuite(self):
        return self.applicationSuite

    def set_availableOnDevice(self, availableOnDevice):
        self.availableOnDevice = availableOnDevice

    def get_availableOnDevice(self):
        return self.availableOnDevice

    def set_countriesNotSupported(self, countriesNotSupported):
        self.countriesNotSupported = countriesNotSupported

    def get_countriesNotSupported(self):
        return self.countriesNotSupported

    def set_countriesSupported(self, countriesSupported):
        self.countriesSupported = countriesSupported

    def get_countriesSupported(self):
        return self.countriesSupported

    def set_downloadUrl(self, downloadUrl):
        self.downloadUrl = downloadUrl

    def get_downloadUrl(self):
        return self.downloadUrl

    def set_featureList(self, featureList):
        self.featureList = featureList

    def get_featureList(self):
        return self.featureList

    def set_fileSize(self, fileSize):
        self.fileSize = fileSize

    def get_fileSize(self):
        return self.fileSize

    def set_installUrl(self, installUrl):
        self.installUrl = installUrl

    def get_installUrl(self):
        return self.installUrl

    def set_memoryRequirements(self, memoryRequirements):
        self.memoryRequirements = memoryRequirements

    def get_memoryRequirements(self):
        return self.memoryRequirements

    def set_operatingSystem(self, operatingSystem):
        self.operatingSystem = operatingSystem

    def get_operatingSystem(self):
        return self.operatingSystem

    def set_permissions(self, permissions):
        self.permissions = permissions

    def get_permissions(self):
        return self.permissions

    def set_processorRequirements(self, processorRequirements):
        self.processorRequirements = processorRequirements

    def get_processorRequirements(self):
        return self.processorRequirements

    def set_releaseNotes(self, releaseNotes):
        self.releaseNotes = releaseNotes

    def get_releaseNotes(self):
        return self.releaseNotes

    def set_screenshot(self, screenshot):
        self.screenshot = screenshot

    def get_screenshot(self):
        return self.screenshot

    def set_softwareAddOn(self, softwareAddOn):
        self.softwareAddOn = softwareAddOn

    def get_softwareAddOn(self):
        return self.softwareAddOn

    def set_softwareHelp(self, softwareHelp):
        self.softwareHelp = softwareHelp

    def get_softwareHelp(self):
        return self.softwareHelp

    def set_softwareRequirements(self, softwareRequirements):
        self.softwareRequirements = softwareRequirements

    def get_softwareRequirements(self):
        return self.softwareRequirements

    def set_softwareVersion(self, softwareVersion):
        self.softwareVersion = softwareVersion

    def get_softwareVersion(self):
        return self.softwareVersion

    def set_storageRequirements(self, storageRequirements):
        self.storageRequirements = storageRequirements

    def get_storageRequirements(self):
        return self.storageRequirements

    def set_supportingData(self, supportingData):
        self.supportingData = supportingData

    def get_supportingData(self):
        return self.supportingData


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
