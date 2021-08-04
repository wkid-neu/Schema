from PreprocessData.all_class_files.DeliveryMethod import DeliveryMethod
import global_data


class LockerDelivery(DeliveryMethod):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None):
        DeliveryMethod.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
