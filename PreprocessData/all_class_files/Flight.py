from PreprocessData.all_class_files.Trip import Trip
import global_data


class Flight(Trip):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, arrivalTime=None, departureTime=None, offers=None, provider=None, aircraft=None, arrivalAirport=None, arrivalGate=None, arrivalTerminal=None, boardingPolicy=None, departureAirport=None, departureGate=None, departureTerminal=None, estimatedFlightDuration=None, flightDistance=None, flightNumber=None, mealService=None, seller=None, webCheckinTime=None):
        Trip.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, arrivalTime, departureTime, offers, provider)
        self.aircraft = aircraft
        self.arrivalAirport = arrivalAirport
        self.arrivalGate = arrivalGate
        self.arrivalTerminal = arrivalTerminal
        self.boardingPolicy = boardingPolicy
        self.departureAirport = departureAirport
        self.departureGate = departureGate
        self.departureTerminal = departureTerminal
        self.estimatedFlightDuration = estimatedFlightDuration
        self.flightDistance = flightDistance
        self.flightNumber = flightNumber
        self.mealService = mealService
        self.seller = seller
        self.webCheckinTime = webCheckinTime

    def set_aircraft(self, aircraft):
        self.aircraft = aircraft

    def get_aircraft(self):
        return self.aircraft

    def set_arrivalAirport(self, arrivalAirport):
        self.arrivalAirport = arrivalAirport

    def get_arrivalAirport(self):
        return self.arrivalAirport

    def set_arrivalGate(self, arrivalGate):
        self.arrivalGate = arrivalGate

    def get_arrivalGate(self):
        return self.arrivalGate

    def set_arrivalTerminal(self, arrivalTerminal):
        self.arrivalTerminal = arrivalTerminal

    def get_arrivalTerminal(self):
        return self.arrivalTerminal

    def set_boardingPolicy(self, boardingPolicy):
        self.boardingPolicy = boardingPolicy

    def get_boardingPolicy(self):
        return self.boardingPolicy

    def set_departureAirport(self, departureAirport):
        self.departureAirport = departureAirport

    def get_departureAirport(self):
        return self.departureAirport

    def set_departureGate(self, departureGate):
        self.departureGate = departureGate

    def get_departureGate(self):
        return self.departureGate

    def set_departureTerminal(self, departureTerminal):
        self.departureTerminal = departureTerminal

    def get_departureTerminal(self):
        return self.departureTerminal

    def set_estimatedFlightDuration(self, estimatedFlightDuration):
        self.estimatedFlightDuration = estimatedFlightDuration

    def get_estimatedFlightDuration(self):
        return self.estimatedFlightDuration

    def set_flightDistance(self, flightDistance):
        self.flightDistance = flightDistance

    def get_flightDistance(self):
        return self.flightDistance

    def set_flightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def get_flightNumber(self):
        return self.flightNumber

    def set_mealService(self, mealService):
        self.mealService = mealService

    def get_mealService(self):
        return self.mealService

    def set_seller(self, seller):
        self.seller = seller

    def get_seller(self):
        return self.seller

    def set_webCheckinTime(self, webCheckinTime):
        self.webCheckinTime = webCheckinTime

    def get_webCheckinTime(self):
        return self.webCheckinTime


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
