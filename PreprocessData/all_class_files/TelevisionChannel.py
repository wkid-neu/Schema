from PreprocessData.all_class_files.BroadcastChannel import BroadcastChannel
import global_data


class TelevisionChannel(BroadcastChannel):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, broadcastChannelId=None, broadcastServiceTier=None, genre=None, inBroadcastLineup=None, providesBroadcastService=None):
        BroadcastChannel.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url, broadcastChannelId, broadcastServiceTier, genre, inBroadcastLineup, providesBroadcastService)
