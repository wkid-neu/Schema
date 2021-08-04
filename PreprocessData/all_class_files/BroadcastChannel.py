from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class BroadcastChannel(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, broadcastChannelId=None, broadcastServiceTier=None, genre=None, inBroadcastLineup=None, providesBroadcastService=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.broadcastChannelId = broadcastChannelId
        self.broadcastServiceTier = broadcastServiceTier
        self.genre = genre
        self.inBroadcastLineup = inBroadcastLineup
        self.providesBroadcastService = providesBroadcastService

    def set_broadcastChannelId(self, broadcastChannelId):
        self.broadcastChannelId = broadcastChannelId

    def get_broadcastChannelId(self):
        return self.broadcastChannelId

    def set_broadcastServiceTier(self, broadcastServiceTier):
        self.broadcastServiceTier = broadcastServiceTier

    def get_broadcastServiceTier(self):
        return self.broadcastServiceTier

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_inBroadcastLineup(self, inBroadcastLineup):
        self.inBroadcastLineup = inBroadcastLineup

    def get_inBroadcastLineup(self):
        return self.inBroadcastLineup

    def set_providesBroadcastService(self, providesBroadcastService):
        self.providesBroadcastService = providesBroadcastService

    def get_providesBroadcastService(self):
        return self.providesBroadcastService


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
