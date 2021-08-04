from PreprocessData.all_class_files.Trip import Trip
import global_data


class BusTrip(Trip):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, arrivalTime=None, departureTime=None, offers=None, provider=None, arrivalBusStop=None, busName=None, busNumber=None, departureBusStop=None):
        Trip.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, arrivalTime, departureTime, offers, provider)
        self.arrivalBusStop = arrivalBusStop
        self.busName = busName
        self.busNumber = busNumber
        self.departureBusStop = departureBusStop

    def set_arrivalBusStop(self, arrivalBusStop):
        self.arrivalBusStop = arrivalBusStop

    def get_arrivalBusStop(self):
        return self.arrivalBusStop

    def set_busName(self, busName):
        self.busName = busName

    def get_busName(self):
        return self.busName

    def set_busNumber(self, busNumber):
        self.busNumber = busNumber

    def get_busNumber(self):
        return self.busNumber

    def set_departureBusStop(self, departureBusStop):
        self.departureBusStop = departureBusStop

    def get_departureBusStop(self):
        return self.departureBusStop


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
