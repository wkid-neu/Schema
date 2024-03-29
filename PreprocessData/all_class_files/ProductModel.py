from PreprocessData.all_class_files.Product import Product
import global_data


class ProductModel(Product):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalProperty=None, aggregateRating=None, audience=None, award=None, brand=None, category=None, color=None, depth=None, gtin12=None, gtin13=None, gtin14=None, gtin8=None, height=None, isAccessoryOrSparePartFor=None, isConsumableFor=None, isRelatedTo=None, isSimilarTo=None, itemCondition=None, logo=None, manufacturer=None, material=None, model=None, mpn=None, offers=None, productID=None, productionDate=None, purchaseDate=None, releaseDate=None, review=None, sku=None, weight=None, width=None, isVariantOf=None, predecessorOf=None, successorOf=None):
        Product.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, additionalProperty, aggregateRating, audience, award, brand, category, color, depth, gtin12, gtin13, gtin14, gtin8, height, isAccessoryOrSparePartFor, isConsumableFor, isRelatedTo, isSimilarTo, itemCondition, logo, manufacturer, material, model, mpn, offers, productID, productionDate, purchaseDate, releaseDate, review, sku, weight, width)
        self.isVariantOf = isVariantOf
        self.predecessorOf = predecessorOf
        self.successorOf = successorOf

    def set_isVariantOf(self, isVariantOf):
        self.isVariantOf = isVariantOf

    def get_isVariantOf(self):
        return self.isVariantOf

    def set_predecessorOf(self, predecessorOf):
        self.predecessorOf = predecessorOf

    def get_predecessorOf(self):
        return self.predecessorOf

    def set_successorOf(self, successorOf):
        self.successorOf = successorOf

    def get_successorOf(self):
        return self.successorOf


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
