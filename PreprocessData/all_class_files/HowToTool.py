from PreprocessData.all_class_files.HowToItem import HowToItem
import global_data


class HowToTool(HowToItem):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, item=None, nextItem=None, position=None, previousItem=None, requiredQuantity=None):
        HowToItem.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, item, nextItem, position, previousItem, requiredQuantity)
