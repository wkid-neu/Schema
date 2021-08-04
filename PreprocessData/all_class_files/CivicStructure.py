from PreprocessData.all_class_files.Place import Place
import global_data


class CivicStructure(Place):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalProperty=None, address=None, aggregateRating=None, amenityFeature=None, branchCode=None, containedInPlace=None, containsPlace=None, event=None, faxNumber=None, geo=None, globalLocationNumber=None, hasMap=None, isAccessibleForFree=None, isicV4=None, logo=None, maximumAttendeeCapacity=None, openingHoursSpecification=None, photo=None, publicAccess=None, review=None, smokingAllowed=None, specialOpeningHoursSpecification=None, telephone=None, openingHours=None):
        Place.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, additionalProperty, address, aggregateRating, amenityFeature, branchCode, containedInPlace, containsPlace, event, faxNumber, geo, globalLocationNumber, hasMap, isAccessibleForFree, isicV4, logo, maximumAttendeeCapacity, openingHoursSpecification, photo, publicAccess, review, smokingAllowed, specialOpeningHoursSpecification, telephone)
        self.openingHours = openingHours

    def set_openingHours(self, openingHours):
        self.openingHours = openingHours

    def get_openingHours(self):
        return self.openingHours


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
