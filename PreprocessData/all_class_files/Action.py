from PreprocessData.all_class_files.Thing import Thing
import global_data


class Action(Thing):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, actionStatus=None, agent=None, endTime=None, error=None, instrument=None, location=None, object=None, participant=None, result=None, startTime=None, target=None):
        Thing.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.actionStatus = actionStatus
        self.agent = agent
        self.endTime = endTime
        self.error = error
        self.instrument = instrument
        self.location = location
        self.object = object
        self.participant = participant
        self.result = result
        self.startTime = startTime
        self.target = target

    def set_actionStatus(self, actionStatus):
        self.actionStatus = actionStatus

    def get_actionStatus(self):
        return self.actionStatus

    def set_agent(self, agent):
        self.agent = agent

    def get_agent(self):
        return self.agent

    def set_endTime(self, endTime):
        self.endTime = endTime

    def get_endTime(self):
        return self.endTime

    def set_error(self, error):
        self.error = error

    def get_error(self):
        return self.error

    def set_instrument(self, instrument):
        self.instrument = instrument

    def get_instrument(self):
        return self.instrument

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_object(self, object):
        self.object = object

    def get_object(self):
        return self.object

    def set_participant(self, participant):
        self.participant = participant

    def get_participant(self):
        return self.participant

    def set_result(self, result):
        self.result = result

    def get_result(self):
        return self.result

    def set_startTime(self, startTime):
        self.startTime = startTime

    def get_startTime(self):
        return self.startTime

    def set_target(self, target):
        self.target = target

    def get_target(self):
        return self.target


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
