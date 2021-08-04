from PreprocessData.all_class_files.HowTo import HowTo
import global_data


class Recipe(HowTo):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, about=None, accessMode=None, accessModeSufficient=None, accessibilityAPI=None, accessibilityControl=None, accessibilityFeature=None, accessibilityHazard=None, accessibilitySummary=None, accountablePerson=None, aggregateRating=None, alternativeHeadline=None, associatedMedia=None, audience=None, audio=None, author=None, award=None, character=None, citation=None, comment=None, commentCount=None, contentLocation=None, contentRating=None, contributor=None, copyrightHolder=None, copyrightYear=None, creator=None, dateCreated=None, dateModified=None, datePublished=None, discussionUrl=None, editor=None, educationalAlignment=None, educationalUse=None, encoding=None, encodingFormat=None, exampleOfWork=None, expires=None, funder=None, genre=None, hasPart=None, headline=None, inLanguage=None, interactionStatistic=None, interactivityType=None, isAccessibleForFree=None, isBasedOn=None, isFamilyFriendly=None, isPartOf=None, keywords=None, learningResourceType=None, license=None, locationCreated=None, mainEntity=None, material=None, mentions=None, offers=None, position=None, producer=None, provider=None, publication=None, publisher=None, publishingPrinciples=None, recordedAt=None, releasedEvent=None, review=None, schemaVersion=None, sourceOrganization=None, spatialCoverage=None, sponsor=None, temporalCoverage=None, text=None, thumbnailUrl=None, timeRequired=None, translator=None, typicalAgeRange=None, version=None, video=None, workExample=None, estimatedCost=None, performTime=None, prepTime=None, step=None, supply=None, tool=None, totalTime=None, yielded=None, cookTime=None, cookingMethod=None, nutrition=None, recipeCategory=None, recipeCuisine=None, recipeIngredient=None, recipeInstructions=None, recipeYield=None, suitableForDiet=None):
        HowTo.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, about, accessMode, accessModeSufficient, accessibilityAPI, accessibilityControl, accessibilityFeature, accessibilityHazard, accessibilitySummary, accountablePerson, aggregateRating, alternativeHeadline, associatedMedia, audience, audio, author, award, character, citation, comment, commentCount, contentLocation, contentRating, contributor, copyrightHolder, copyrightYear, creator, dateCreated, dateModified, datePublished, discussionUrl, editor, educationalAlignment, educationalUse, encoding, encodingFormat, exampleOfWork, expires, funder, genre, hasPart, headline, inLanguage, interactionStatistic, interactivityType, isAccessibleForFree, isBasedOn, isFamilyFriendly, isPartOf, keywords, learningResourceType, license, locationCreated, mainEntity, material, mentions, offers, position, producer, provider, publication, publisher, publishingPrinciples, recordedAt, releasedEvent, review, schemaVersion, sourceOrganization, spatialCoverage, sponsor, temporalCoverage, text, thumbnailUrl, timeRequired, translator, typicalAgeRange, version, video, workExample, estimatedCost, performTime, prepTime, step, supply, tool, totalTime, yielded)
        self.cookTime = cookTime
        self.cookingMethod = cookingMethod
        self.nutrition = nutrition
        self.recipeCategory = recipeCategory
        self.recipeCuisine = recipeCuisine
        self.recipeIngredient = recipeIngredient
        self.recipeInstructions = recipeInstructions
        self.recipeYield = recipeYield
        self.suitableForDiet = suitableForDiet

    def set_cookTime(self, cookTime):
        self.cookTime = cookTime

    def get_cookTime(self):
        return self.cookTime

    def set_cookingMethod(self, cookingMethod):
        self.cookingMethod = cookingMethod

    def get_cookingMethod(self):
        return self.cookingMethod

    def set_nutrition(self, nutrition):
        self.nutrition = nutrition

    def get_nutrition(self):
        return self.nutrition

    def set_recipeCategory(self, recipeCategory):
        self.recipeCategory = recipeCategory

    def get_recipeCategory(self):
        return self.recipeCategory

    def set_recipeCuisine(self, recipeCuisine):
        self.recipeCuisine = recipeCuisine

    def get_recipeCuisine(self):
        return self.recipeCuisine

    def set_recipeIngredient(self, recipeIngredient):
        self.recipeIngredient = recipeIngredient

    def get_recipeIngredient(self):
        return self.recipeIngredient

    def set_recipeInstructions(self, recipeInstructions):
        self.recipeInstructions = recipeInstructions

    def get_recipeInstructions(self):
        return self.recipeInstructions

    def set_recipeYield(self, recipeYield):
        self.recipeYield = recipeYield

    def get_recipeYield(self):
        return self.recipeYield

    def set_suitableForDiet(self, suitableForDiet):
        self.suitableForDiet = suitableForDiet

    def get_suitableForDiet(self):
        return self.suitableForDiet


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
