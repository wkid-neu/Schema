from PreprocessData.all_class_files.CreateAction import CreateAction
import global_data


class CookAction(CreateAction):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, actionStatus=None, agent=None, endTime=None, error=None, instrument=None, location=None, object=None, participant=None, result=None, startTime=None, target=None, foodEstablishment=None, foodEvent=None, recipe=None):
        CreateAction.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, actionStatus, agent, endTime, error, instrument, location, object, participant, result, startTime, target)
        self.foodEstablishment = foodEstablishment
        self.foodEvent = foodEvent
        self.recipe = recipe

    def set_foodEstablishment(self, foodEstablishment):
        self.foodEstablishment = foodEstablishment

    def get_foodEstablishment(self):
        return self.foodEstablishment

    def set_foodEvent(self, foodEvent):
        self.foodEvent = foodEvent

    def get_foodEvent(self):
        return self.foodEvent

    def set_recipe(self, recipe):
        self.recipe = recipe

    def get_recipe(self):
        return self.recipe


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
