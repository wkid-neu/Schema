from PreprocessData.all_class_files.Permit import Permit
import global_data


class GovernmentPermit(Permit):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, issuedBy=None, issuedThrough=None, permitAudience=None, validFor=None, validFrom=None, validIn=None, validUntil=None):
        Permit.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, issuedBy, issuedThrough, permitAudience, validFor, validFrom, validIn, validUntil)
