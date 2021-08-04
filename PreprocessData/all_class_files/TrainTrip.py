from PreprocessData.all_class_files.Trip import Trip
import global_data


class TrainTrip(Trip):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, arrivalTime=None, departureTime=None, offers=None, provider=None, arrivalPlatform=None, arrivalStation=None, departurePlatform=None, departureStation=None, trainName=None, trainNumber=None):
        Trip.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, arrivalTime, departureTime, offers, provider)
        self.arrivalPlatform = arrivalPlatform
        self.arrivalStation = arrivalStation
        self.departurePlatform = departurePlatform
        self.departureStation = departureStation
        self.trainName = trainName
        self.trainNumber = trainNumber

    def set_arrivalPlatform(self, arrivalPlatform):
        self.arrivalPlatform = arrivalPlatform

    def get_arrivalPlatform(self):
        return self.arrivalPlatform

    def set_arrivalStation(self, arrivalStation):
        self.arrivalStation = arrivalStation

    def get_arrivalStation(self):
        return self.arrivalStation

    def set_departurePlatform(self, departurePlatform):
        self.departurePlatform = departurePlatform

    def get_departurePlatform(self):
        return self.departurePlatform

    def set_departureStation(self, departureStation):
        self.departureStation = departureStation

    def get_departureStation(self):
        return self.departureStation

    def set_trainName(self, trainName):
        self.trainName = trainName

    def get_trainName(self):
        return self.trainName

    def set_trainNumber(self, trainNumber):
        self.trainNumber = trainNumber

    def get_trainNumber(self):
        return self.trainNumber


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
