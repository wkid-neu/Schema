from PreprocessData.all_class_files.Thing import Thing
import global_data


class Place(Thing):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalProperty=None, address=None, aggregateRating=None, amenityFeature=None, branchCode=None, containedInPlace=None, containsPlace=None, event=None, faxNumber=None, geo=None, globalLocationNumber=None, hasMap=None, isAccessibleForFree=None, isicV4=None, logo=None, maximumAttendeeCapacity=None, openingHoursSpecification=None, photo=None, publicAccess=None, review=None, smokingAllowed=None, specialOpeningHoursSpecification=None, telephone=None):
        Thing.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.additionalProperty = additionalProperty
        self.address = address
        self.aggregateRating = aggregateRating
        self.amenityFeature = amenityFeature
        self.branchCode = branchCode
        self.containedInPlace = containedInPlace
        self.containsPlace = containsPlace
        self.event = event
        self.faxNumber = faxNumber
        self.geo = geo
        self.globalLocationNumber = globalLocationNumber
        self.hasMap = hasMap
        self.isAccessibleForFree = isAccessibleForFree
        self.isicV4 = isicV4
        self.logo = logo
        self.maximumAttendeeCapacity = maximumAttendeeCapacity
        self.openingHoursSpecification = openingHoursSpecification
        self.photo = photo
        self.publicAccess = publicAccess
        self.review = review
        self.smokingAllowed = smokingAllowed
        self.specialOpeningHoursSpecification = specialOpeningHoursSpecification
        self.telephone = telephone

    def set_additionalProperty(self, additionalProperty):
        self.additionalProperty = additionalProperty

    def get_additionalProperty(self):
        return self.additionalProperty

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_aggregateRating(self, aggregateRating):
        self.aggregateRating = aggregateRating

    def get_aggregateRating(self):
        return self.aggregateRating

    def set_amenityFeature(self, amenityFeature):
        self.amenityFeature = amenityFeature

    def get_amenityFeature(self):
        return self.amenityFeature

    def set_branchCode(self, branchCode):
        self.branchCode = branchCode

    def get_branchCode(self):
        return self.branchCode

    def set_containedInPlace(self, containedInPlace):
        self.containedInPlace = containedInPlace

    def get_containedInPlace(self):
        return self.containedInPlace

    def set_containsPlace(self, containsPlace):
        self.containsPlace = containsPlace

    def get_containsPlace(self):
        return self.containsPlace

    def set_event(self, event):
        self.event = event

    def get_event(self):
        return self.event

    def set_faxNumber(self, faxNumber):
        self.faxNumber = faxNumber

    def get_faxNumber(self):
        return self.faxNumber

    def set_geo(self, geo):
        self.geo = geo

    def get_geo(self):
        return self.geo

    def set_globalLocationNumber(self, globalLocationNumber):
        self.globalLocationNumber = globalLocationNumber

    def get_globalLocationNumber(self):
        return self.globalLocationNumber

    def set_hasMap(self, hasMap):
        self.hasMap = hasMap

    def get_hasMap(self):
        return self.hasMap

    def set_isAccessibleForFree(self, isAccessibleForFree):
        self.isAccessibleForFree = isAccessibleForFree

    def get_isAccessibleForFree(self):
        return self.isAccessibleForFree

    def set_isicV4(self, isicV4):
        self.isicV4 = isicV4

    def get_isicV4(self):
        return self.isicV4

    def set_logo(self, logo):
        self.logo = logo

    def get_logo(self):
        return self.logo

    def set_maximumAttendeeCapacity(self, maximumAttendeeCapacity):
        self.maximumAttendeeCapacity = maximumAttendeeCapacity

    def get_maximumAttendeeCapacity(self):
        return self.maximumAttendeeCapacity

    def set_openingHoursSpecification(self, openingHoursSpecification):
        self.openingHoursSpecification = openingHoursSpecification

    def get_openingHoursSpecification(self):
        return self.openingHoursSpecification

    def set_photo(self, photo):
        self.photo = photo

    def get_photo(self):
        return self.photo

    def set_publicAccess(self, publicAccess):
        self.publicAccess = publicAccess

    def get_publicAccess(self):
        return self.publicAccess

    def set_review(self, review):
        self.review = review

    def get_review(self):
        return self.review

    def set_smokingAllowed(self, smokingAllowed):
        self.smokingAllowed = smokingAllowed

    def get_smokingAllowed(self):
        return self.smokingAllowed

    def set_specialOpeningHoursSpecification(self, specialOpeningHoursSpecification):
        self.specialOpeningHoursSpecification = specialOpeningHoursSpecification

    def get_specialOpeningHoursSpecification(self):
        return self.specialOpeningHoursSpecification

    def set_telephone(self, telephone):
        self.telephone = telephone

    def get_telephone(self):
        return self.telephone


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
