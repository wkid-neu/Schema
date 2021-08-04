from PreprocessData.all_class_files.Thing import Thing
import global_data


class Product(Thing):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalProperty=None, aggregateRating=None, audience=None, award=None, brand=None, category=None, color=None, depth=None, gtin12=None, gtin13=None, gtin14=None, gtin8=None, height=None, isAccessoryOrSparePartFor=None, isConsumableFor=None, isRelatedTo=None, isSimilarTo=None, itemCondition=None, logo=None, manufacturer=None, material=None, model=None, mpn=None, offers=None, productID=None, productionDate=None, purchaseDate=None, releaseDate=None, review=None, sku=None, weight=None, width=None):
        Thing.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.additionalProperty = additionalProperty
        self.aggregateRating = aggregateRating
        self.audience = audience
        self.award = award
        self.brand = brand
        self.category = category
        self.color = color
        self.depth = depth
        self.gtin12 = gtin12
        self.gtin13 = gtin13
        self.gtin14 = gtin14
        self.gtin8 = gtin8
        self.height = height
        self.isAccessoryOrSparePartFor = isAccessoryOrSparePartFor
        self.isConsumableFor = isConsumableFor
        self.isRelatedTo = isRelatedTo
        self.isSimilarTo = isSimilarTo
        self.itemCondition = itemCondition
        self.logo = logo
        self.manufacturer = manufacturer
        self.material = material
        self.model = model
        self.mpn = mpn
        self.offers = offers
        self.productID = productID
        self.productionDate = productionDate
        self.purchaseDate = purchaseDate
        self.releaseDate = releaseDate
        self.review = review
        self.sku = sku
        self.weight = weight
        self.width = width

    def set_additionalProperty(self, additionalProperty):
        self.additionalProperty = additionalProperty

    def get_additionalProperty(self):
        return self.additionalProperty

    def set_aggregateRating(self, aggregateRating):
        self.aggregateRating = aggregateRating

    def get_aggregateRating(self):
        return self.aggregateRating

    def set_audience(self, audience):
        self.audience = audience

    def get_audience(self):
        return self.audience

    def set_award(self, award):
        self.award = award

    def get_award(self):
        return self.award

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth

    def set_gtin12(self, gtin12):
        self.gtin12 = gtin12

    def get_gtin12(self):
        return self.gtin12

    def set_gtin13(self, gtin13):
        self.gtin13 = gtin13

    def get_gtin13(self):
        return self.gtin13

    def set_gtin14(self, gtin14):
        self.gtin14 = gtin14

    def get_gtin14(self):
        return self.gtin14

    def set_gtin8(self, gtin8):
        self.gtin8 = gtin8

    def get_gtin8(self):
        return self.gtin8

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_isAccessoryOrSparePartFor(self, isAccessoryOrSparePartFor):
        self.isAccessoryOrSparePartFor = isAccessoryOrSparePartFor

    def get_isAccessoryOrSparePartFor(self):
        return self.isAccessoryOrSparePartFor

    def set_isConsumableFor(self, isConsumableFor):
        self.isConsumableFor = isConsumableFor

    def get_isConsumableFor(self):
        return self.isConsumableFor

    def set_isRelatedTo(self, isRelatedTo):
        self.isRelatedTo = isRelatedTo

    def get_isRelatedTo(self):
        return self.isRelatedTo

    def set_isSimilarTo(self, isSimilarTo):
        self.isSimilarTo = isSimilarTo

    def get_isSimilarTo(self):
        return self.isSimilarTo

    def set_itemCondition(self, itemCondition):
        self.itemCondition = itemCondition

    def get_itemCondition(self):
        return self.itemCondition

    def set_logo(self, logo):
        self.logo = logo

    def get_logo(self):
        return self.logo

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_material(self, material):
        self.material = material

    def get_material(self):
        return self.material

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_mpn(self, mpn):
        self.mpn = mpn

    def get_mpn(self):
        return self.mpn

    def set_offers(self, offers):
        self.offers = offers

    def get_offers(self):
        return self.offers

    def set_productID(self, productID):
        self.productID = productID

    def get_productID(self):
        return self.productID

    def set_productionDate(self, productionDate):
        self.productionDate = productionDate

    def get_productionDate(self):
        return self.productionDate

    def set_purchaseDate(self, purchaseDate):
        self.purchaseDate = purchaseDate

    def get_purchaseDate(self):
        return self.purchaseDate

    def set_releaseDate(self, releaseDate):
        self.releaseDate = releaseDate

    def get_releaseDate(self):
        return self.releaseDate

    def set_review(self, review):
        self.review = review

    def get_review(self):
        return self.review

    def set_sku(self, sku):
        self.sku = sku

    def get_sku(self):
        return self.sku

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
