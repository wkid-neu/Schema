from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Order(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, acceptedOffer=None, billingAddress=None, broker=None, confirmationNumber=None, customer=None, discount=None, discountCode=None, discountCurrency=None, isGift=None, orderDate=None, orderDelivery=None, orderNumber=None, orderStatus=None, orderedItem=None, partOfInvoice=None, paymentDueDate=None, paymentMethod=None, paymentMethodId=None, paymentUrl=None, seller=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.acceptedOffer = acceptedOffer
        self.billingAddress = billingAddress
        self.broker = broker
        self.confirmationNumber = confirmationNumber
        self.customer = customer
        self.discount = discount
        self.discountCode = discountCode
        self.discountCurrency = discountCurrency
        self.isGift = isGift
        self.orderDate = orderDate
        self.orderDelivery = orderDelivery
        self.orderNumber = orderNumber
        self.orderStatus = orderStatus
        self.orderedItem = orderedItem
        self.partOfInvoice = partOfInvoice
        self.paymentDueDate = paymentDueDate
        self.paymentMethod = paymentMethod
        self.paymentMethodId = paymentMethodId
        self.paymentUrl = paymentUrl
        self.seller = seller

    def set_acceptedOffer(self, acceptedOffer):
        self.acceptedOffer = acceptedOffer

    def get_acceptedOffer(self):
        return self.acceptedOffer

    def set_billingAddress(self, billingAddress):
        self.billingAddress = billingAddress

    def get_billingAddress(self):
        return self.billingAddress

    def set_broker(self, broker):
        self.broker = broker

    def get_broker(self):
        return self.broker

    def set_confirmationNumber(self, confirmationNumber):
        self.confirmationNumber = confirmationNumber

    def get_confirmationNumber(self):
        return self.confirmationNumber

    def set_customer(self, customer):
        self.customer = customer

    def get_customer(self):
        return self.customer

    def set_discount(self, discount):
        self.discount = discount

    def get_discount(self):
        return self.discount

    def set_discountCode(self, discountCode):
        self.discountCode = discountCode

    def get_discountCode(self):
        return self.discountCode

    def set_discountCurrency(self, discountCurrency):
        self.discountCurrency = discountCurrency

    def get_discountCurrency(self):
        return self.discountCurrency

    def set_isGift(self, isGift):
        self.isGift = isGift

    def get_isGift(self):
        return self.isGift

    def set_orderDate(self, orderDate):
        self.orderDate = orderDate

    def get_orderDate(self):
        return self.orderDate

    def set_orderDelivery(self, orderDelivery):
        self.orderDelivery = orderDelivery

    def get_orderDelivery(self):
        return self.orderDelivery

    def set_orderNumber(self, orderNumber):
        self.orderNumber = orderNumber

    def get_orderNumber(self):
        return self.orderNumber

    def set_orderStatus(self, orderStatus):
        self.orderStatus = orderStatus

    def get_orderStatus(self):
        return self.orderStatus

    def set_orderedItem(self, orderedItem):
        self.orderedItem = orderedItem

    def get_orderedItem(self):
        return self.orderedItem

    def set_partOfInvoice(self, partOfInvoice):
        self.partOfInvoice = partOfInvoice

    def get_partOfInvoice(self):
        return self.partOfInvoice

    def set_paymentDueDate(self, paymentDueDate):
        self.paymentDueDate = paymentDueDate

    def get_paymentDueDate(self):
        return self.paymentDueDate

    def set_paymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod

    def get_paymentMethod(self):
        return self.paymentMethod

    def set_paymentMethodId(self, paymentMethodId):
        self.paymentMethodId = paymentMethodId

    def get_paymentMethodId(self):
        return self.paymentMethodId

    def set_paymentUrl(self, paymentUrl):
        self.paymentUrl = paymentUrl

    def get_paymentUrl(self):
        return self.paymentUrl

    def set_seller(self, seller):
        self.seller = seller

    def get_seller(self):
        return self.seller


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
