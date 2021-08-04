from PreprocessData.all_class_files.TradeAction import TradeAction
import global_data


class RentAction(TradeAction):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, actionStatus=None, agent=None, endTime=None, error=None, instrument=None, location=None, object=None, participant=None, result=None, startTime=None, target=None, price=None, priceSpecification=None, landlord=None, realEstateAgent=None):
        TradeAction.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, actionStatus, agent, endTime, error, instrument, location, object, participant, result, startTime, target, price, priceSpecification)
        self.landlord = landlord
        self.realEstateAgent = realEstateAgent

    def set_landlord(self, landlord):
        self.landlord = landlord

    def get_landlord(self):
        return self.landlord

    def set_realEstateAgent(self, realEstateAgent):
        self.realEstateAgent = realEstateAgent

    def get_realEstateAgent(self):
        return self.realEstateAgent


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
