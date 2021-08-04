from PreprocessData.all_class_files.PlayAction import PlayAction
import global_data


class ExerciseAction(PlayAction):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, actionStatus=None, agent=None, endTime=None, error=None, instrument=None, location=None, object=None, participant=None, result=None, startTime=None, target=None, audience=None, event=None, distance=None, exerciseCourse=None, fromLocation=None, opponent=None, sportsActivityLocation=None, sportsEvent=None, sportsTeam=None, toLocation=None):
        PlayAction.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, actionStatus, agent, endTime, error, instrument, location, object, participant, result, startTime, target, audience, event)
        self.distance = distance
        self.exerciseCourse = exerciseCourse
        self.fromLocation = fromLocation
        self.opponent = opponent
        self.sportsActivityLocation = sportsActivityLocation
        self.sportsEvent = sportsEvent
        self.sportsTeam = sportsTeam
        self.toLocation = toLocation

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_exerciseCourse(self, exerciseCourse):
        self.exerciseCourse = exerciseCourse

    def get_exerciseCourse(self):
        return self.exerciseCourse

    def set_fromLocation(self, fromLocation):
        self.fromLocation = fromLocation

    def get_fromLocation(self):
        return self.fromLocation

    def set_opponent(self, opponent):
        self.opponent = opponent

    def get_opponent(self):
        return self.opponent

    def set_sportsActivityLocation(self, sportsActivityLocation):
        self.sportsActivityLocation = sportsActivityLocation

    def get_sportsActivityLocation(self):
        return self.sportsActivityLocation

    def set_sportsEvent(self, sportsEvent):
        self.sportsEvent = sportsEvent

    def get_sportsEvent(self):
        return self.sportsEvent

    def set_sportsTeam(self, sportsTeam):
        self.sportsTeam = sportsTeam

    def get_sportsTeam(self):
        return self.sportsTeam

    def set_toLocation(self, toLocation):
        self.toLocation = toLocation

    def get_toLocation(self):
        return self.toLocation


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
