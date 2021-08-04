from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class Invoice(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, accountId=None, billingPeriod=None, broker=None, category=None, confirmationNumber=None, customer=None, minimumPaymentDue=None, paymentDueDate=None, paymentMethod=None, paymentMethodId=None, paymentStatus=None, provider=None, referencesOrder=None, scheduledPaymentDate=None, totalPaymentDue=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.accountId = accountId
        self.billingPeriod = billingPeriod
        self.broker = broker
        self.category = category
        self.confirmationNumber = confirmationNumber
        self.customer = customer
        self.minimumPaymentDue = minimumPaymentDue
        self.paymentDueDate = paymentDueDate
        self.paymentMethod = paymentMethod
        self.paymentMethodId = paymentMethodId
        self.paymentStatus = paymentStatus
        self.provider = provider
        self.referencesOrder = referencesOrder
        self.scheduledPaymentDate = scheduledPaymentDate
        self.totalPaymentDue = totalPaymentDue

    def set_accountId(self, accountId):
        self.accountId = accountId

    def get_accountId(self):
        return self.accountId

    def set_billingPeriod(self, billingPeriod):
        self.billingPeriod = billingPeriod

    def get_billingPeriod(self):
        return self.billingPeriod

    def set_broker(self, broker):
        self.broker = broker

    def get_broker(self):
        return self.broker

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_confirmationNumber(self, confirmationNumber):
        self.confirmationNumber = confirmationNumber

    def get_confirmationNumber(self):
        return self.confirmationNumber

    def set_customer(self, customer):
        self.customer = customer

    def get_customer(self):
        return self.customer

    def set_minimumPaymentDue(self, minimumPaymentDue):
        self.minimumPaymentDue = minimumPaymentDue

    def get_minimumPaymentDue(self):
        return self.minimumPaymentDue

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

    def set_paymentStatus(self, paymentStatus):
        self.paymentStatus = paymentStatus

    def get_paymentStatus(self):
        return self.paymentStatus

    def set_provider(self, provider):
        self.provider = provider

    def get_provider(self):
        return self.provider

    def set_referencesOrder(self, referencesOrder):
        self.referencesOrder = referencesOrder

    def get_referencesOrder(self):
        return self.referencesOrder

    def set_scheduledPaymentDate(self, scheduledPaymentDate):
        self.scheduledPaymentDate = scheduledPaymentDate

    def get_scheduledPaymentDate(self):
        return self.scheduledPaymentDate

    def set_totalPaymentDue(self, totalPaymentDue):
        self.totalPaymentDue = totalPaymentDue

    def get_totalPaymentDue(self):
        return self.totalPaymentDue


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
