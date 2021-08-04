from PreprocessData.all_class_files.Product import Product
import global_data


class Vehicle(Product):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, additionalProperty=None, aggregateRating=None, audience=None, award=None, brand=None, category=None, color=None, depth=None, gtin12=None, gtin13=None, gtin14=None, gtin8=None, height=None, isAccessoryOrSparePartFor=None, isConsumableFor=None, isRelatedTo=None, isSimilarTo=None, itemCondition=None, logo=None, manufacturer=None, material=None, model=None, mpn=None, offers=None, productID=None, productionDate=None, purchaseDate=None, releaseDate=None, review=None, sku=None, weight=None, width=None, cargoVolume=None, dateVehicleFirstRegistered=None, driveWheelConfiguration=None, fuelConsumption=None, fuelEfficiency=None, fuelType=None, knownVehicleDamages=None, mileageFromOdometer=None, numberOfAirbags=None, numberOfAxles=None, numberOfDoors=None, numberOfForwardGears=None, numberOfPreviousOwners=None, steeringPosition=None, vehicleConfiguration=None, vehicleEngine=None, vehicleIdentificationNumber=None, vehicleInteriorColor=None, vehicleInteriorType=None, vehicleModelDate=None, vehicleSeatingCapacity=None, vehicleSpecialUsage=None, vehicleTransmission=None):
        Product.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, additionalProperty, aggregateRating, audience, award, brand, category, color, depth, gtin12, gtin13, gtin14, gtin8, height, isAccessoryOrSparePartFor, isConsumableFor, isRelatedTo, isSimilarTo, itemCondition, logo, manufacturer, material, model, mpn, offers, productID, productionDate, purchaseDate, releaseDate, review, sku, weight, width)
        self.cargoVolume = cargoVolume
        self.dateVehicleFirstRegistered = dateVehicleFirstRegistered
        self.driveWheelConfiguration = driveWheelConfiguration
        self.fuelConsumption = fuelConsumption
        self.fuelEfficiency = fuelEfficiency
        self.fuelType = fuelType
        self.knownVehicleDamages = knownVehicleDamages
        self.mileageFromOdometer = mileageFromOdometer
        self.numberOfAirbags = numberOfAirbags
        self.numberOfAxles = numberOfAxles
        self.numberOfDoors = numberOfDoors
        self.numberOfForwardGears = numberOfForwardGears
        self.numberOfPreviousOwners = numberOfPreviousOwners
        self.productionDate = productionDate
        self.purchaseDate = purchaseDate
        self.steeringPosition = steeringPosition
        self.vehicleConfiguration = vehicleConfiguration
        self.vehicleEngine = vehicleEngine
        self.vehicleIdentificationNumber = vehicleIdentificationNumber
        self.vehicleInteriorColor = vehicleInteriorColor
        self.vehicleInteriorType = vehicleInteriorType
        self.vehicleModelDate = vehicleModelDate
        self.vehicleSeatingCapacity = vehicleSeatingCapacity
        self.vehicleSpecialUsage = vehicleSpecialUsage
        self.vehicleTransmission = vehicleTransmission

    def set_cargoVolume(self, cargoVolume):
        self.cargoVolume = cargoVolume

    def get_cargoVolume(self):
        return self.cargoVolume

    def set_dateVehicleFirstRegistered(self, dateVehicleFirstRegistered):
        self.dateVehicleFirstRegistered = dateVehicleFirstRegistered

    def get_dateVehicleFirstRegistered(self):
        return self.dateVehicleFirstRegistered

    def set_driveWheelConfiguration(self, driveWheelConfiguration):
        self.driveWheelConfiguration = driveWheelConfiguration

    def get_driveWheelConfiguration(self):
        return self.driveWheelConfiguration

    def set_fuelConsumption(self, fuelConsumption):
        self.fuelConsumption = fuelConsumption

    def get_fuelConsumption(self):
        return self.fuelConsumption

    def set_fuelEfficiency(self, fuelEfficiency):
        self.fuelEfficiency = fuelEfficiency

    def get_fuelEfficiency(self):
        return self.fuelEfficiency

    def set_fuelType(self, fuelType):
        self.fuelType = fuelType

    def get_fuelType(self):
        return self.fuelType

    def set_knownVehicleDamages(self, knownVehicleDamages):
        self.knownVehicleDamages = knownVehicleDamages

    def get_knownVehicleDamages(self):
        return self.knownVehicleDamages

    def set_mileageFromOdometer(self, mileageFromOdometer):
        self.mileageFromOdometer = mileageFromOdometer

    def get_mileageFromOdometer(self):
        return self.mileageFromOdometer

    def set_numberOfAirbags(self, numberOfAirbags):
        self.numberOfAirbags = numberOfAirbags

    def get_numberOfAirbags(self):
        return self.numberOfAirbags

    def set_numberOfAxles(self, numberOfAxles):
        self.numberOfAxles = numberOfAxles

    def get_numberOfAxles(self):
        return self.numberOfAxles

    def set_numberOfDoors(self, numberOfDoors):
        self.numberOfDoors = numberOfDoors

    def get_numberOfDoors(self):
        return self.numberOfDoors

    def set_numberOfForwardGears(self, numberOfForwardGears):
        self.numberOfForwardGears = numberOfForwardGears

    def get_numberOfForwardGears(self):
        return self.numberOfForwardGears

    def set_numberOfPreviousOwners(self, numberOfPreviousOwners):
        self.numberOfPreviousOwners = numberOfPreviousOwners

    def get_numberOfPreviousOwners(self):
        return self.numberOfPreviousOwners

    def set_productionDate(self, productionDate):
        self.productionDate = productionDate

    def get_productionDate(self):
        return self.productionDate

    def set_purchaseDate(self, purchaseDate):
        self.purchaseDate = purchaseDate

    def get_purchaseDate(self):
        return self.purchaseDate

    def set_steeringPosition(self, steeringPosition):
        self.steeringPosition = steeringPosition

    def get_steeringPosition(self):
        return self.steeringPosition

    def set_vehicleConfiguration(self, vehicleConfiguration):
        self.vehicleConfiguration = vehicleConfiguration

    def get_vehicleConfiguration(self):
        return self.vehicleConfiguration

    def set_vehicleEngine(self, vehicleEngine):
        self.vehicleEngine = vehicleEngine

    def get_vehicleEngine(self):
        return self.vehicleEngine

    def set_vehicleIdentificationNumber(self, vehicleIdentificationNumber):
        self.vehicleIdentificationNumber = vehicleIdentificationNumber

    def get_vehicleIdentificationNumber(self):
        return self.vehicleIdentificationNumber

    def set_vehicleInteriorColor(self, vehicleInteriorColor):
        self.vehicleInteriorColor = vehicleInteriorColor

    def get_vehicleInteriorColor(self):
        return self.vehicleInteriorColor

    def set_vehicleInteriorType(self, vehicleInteriorType):
        self.vehicleInteriorType = vehicleInteriorType

    def get_vehicleInteriorType(self):
        return self.vehicleInteriorType

    def set_vehicleModelDate(self, vehicleModelDate):
        self.vehicleModelDate = vehicleModelDate

    def get_vehicleModelDate(self):
        return self.vehicleModelDate

    def set_vehicleSeatingCapacity(self, vehicleSeatingCapacity):
        self.vehicleSeatingCapacity = vehicleSeatingCapacity

    def get_vehicleSeatingCapacity(self):
        return self.vehicleSeatingCapacity

    def set_vehicleSpecialUsage(self, vehicleSpecialUsage):
        self.vehicleSpecialUsage = vehicleSpecialUsage

    def get_vehicleSpecialUsage(self):
        return self.vehicleSpecialUsage

    def set_vehicleTransmission(self, vehicleTransmission):
        self.vehicleTransmission = vehicleTransmission

    def get_vehicleTransmission(self):
        return self.vehicleTransmission


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
