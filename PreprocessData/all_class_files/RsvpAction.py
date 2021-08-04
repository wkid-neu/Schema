from PreprocessData.all_class_files.InformAction import InformAction
import global_data


class RsvpAction(InformAction):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, actionStatus=None, agent=None, endTime=None, error=None, instrument=None, location=None, object=None, participant=None, result=None, startTime=None, target=None, about=None, inLanguage=None, recipient=None, event=None, additionalNumberOfGuests=None, comment=None, rsvpResponse=None):
        InformAction.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, actionStatus, agent, endTime, error, instrument, location, object, participant, result, startTime, target, about, inLanguage, recipient, event)
        self.additionalNumberOfGuests = additionalNumberOfGuests
        self.comment = comment
        self.rsvpResponse = rsvpResponse

    def set_additionalNumberOfGuests(self, additionalNumberOfGuests):
        self.additionalNumberOfGuests = additionalNumberOfGuests

    def get_additionalNumberOfGuests(self):
        return self.additionalNumberOfGuests

    def set_comment(self, comment):
        self.comment = comment

    def get_comment(self):
        return self.comment

    def set_rsvpResponse(self, rsvpResponse):
        self.rsvpResponse = rsvpResponse

    def get_rsvpResponse(self):
        return self.rsvpResponse


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
