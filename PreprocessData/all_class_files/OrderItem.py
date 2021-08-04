from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class OrderItem(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, orderDelivery=None, orderItemNumber=None, orderItemStatus=None, orderQuantity=None, orderedItem=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.orderDelivery = orderDelivery
        self.orderItemNumber = orderItemNumber
        self.orderItemStatus = orderItemStatus
        self.orderQuantity = orderQuantity
        self.orderedItem = orderedItem

    def set_orderDelivery(self, orderDelivery):
        self.orderDelivery = orderDelivery

    def get_orderDelivery(self):
        return self.orderDelivery

    def set_orderItemNumber(self, orderItemNumber):
        self.orderItemNumber = orderItemNumber

    def get_orderItemNumber(self):
        return self.orderItemNumber

    def set_orderItemStatus(self, orderItemStatus):
        self.orderItemStatus = orderItemStatus

    def get_orderItemStatus(self):
        return self.orderItemStatus

    def set_orderQuantity(self, orderQuantity):
        self.orderQuantity = orderQuantity

    def get_orderQuantity(self):
        return self.orderQuantity

    def set_orderedItem(self, orderedItem):
        self.orderedItem = orderedItem

    def get_orderedItem(self):
        return self.orderedItem


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
