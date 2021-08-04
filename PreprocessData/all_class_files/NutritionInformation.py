from PreprocessData.all_class_files.StructuredValue import StructuredValue
import global_data


class NutritionInformation(StructuredValue):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, calories=None, carbohydrateContent=None, cholesterolContent=None, fatContent=None, fiberContent=None, proteinContent=None, saturatedFatContent=None, servingSize=None, sodiumContent=None, sugarContent=None, transFatContent=None, unsaturatedFatContent=None):
        StructuredValue.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.calories = calories
        self.carbohydrateContent = carbohydrateContent
        self.cholesterolContent = cholesterolContent
        self.fatContent = fatContent
        self.fiberContent = fiberContent
        self.proteinContent = proteinContent
        self.saturatedFatContent = saturatedFatContent
        self.servingSize = servingSize
        self.sodiumContent = sodiumContent
        self.sugarContent = sugarContent
        self.transFatContent = transFatContent
        self.unsaturatedFatContent = unsaturatedFatContent

    def set_calories(self, calories):
        self.calories = calories

    def get_calories(self):
        return self.calories

    def set_carbohydrateContent(self, carbohydrateContent):
        self.carbohydrateContent = carbohydrateContent

    def get_carbohydrateContent(self):
        return self.carbohydrateContent

    def set_cholesterolContent(self, cholesterolContent):
        self.cholesterolContent = cholesterolContent

    def get_cholesterolContent(self):
        return self.cholesterolContent

    def set_fatContent(self, fatContent):
        self.fatContent = fatContent

    def get_fatContent(self):
        return self.fatContent

    def set_fiberContent(self, fiberContent):
        self.fiberContent = fiberContent

    def get_fiberContent(self):
        return self.fiberContent

    def set_proteinContent(self, proteinContent):
        self.proteinContent = proteinContent

    def get_proteinContent(self):
        return self.proteinContent

    def set_saturatedFatContent(self, saturatedFatContent):
        self.saturatedFatContent = saturatedFatContent

    def get_saturatedFatContent(self):
        return self.saturatedFatContent

    def set_servingSize(self, servingSize):
        self.servingSize = servingSize

    def get_servingSize(self):
        return self.servingSize

    def set_sodiumContent(self, sodiumContent):
        self.sodiumContent = sodiumContent

    def get_sodiumContent(self):
        return self.sodiumContent

    def set_sugarContent(self, sugarContent):
        self.sugarContent = sugarContent

    def get_sugarContent(self):
        return self.sugarContent

    def set_transFatContent(self, transFatContent):
        self.transFatContent = transFatContent

    def get_transFatContent(self):
        return self.transFatContent

    def set_unsaturatedFatContent(self, unsaturatedFatContent):
        self.unsaturatedFatContent = unsaturatedFatContent

    def get_unsaturatedFatContent(self):
        return self.unsaturatedFatContent


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
