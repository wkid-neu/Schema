from PreprocessData.all_class_files.Intangible import Intangible
import global_data


class GameServer(Intangible):
    def __init__(self, additionalType=None, alternateName=None, description=None, disambiguatingDescription=None, identifier=None, image=None, mainEntityOfPage=None, name=None, potentialAction=None, sameAs=None, url=None, game=None, playersOnline=None, serverStatus=None):
        Intangible.__init__(self, additionalType, alternateName, description, disambiguatingDescription, identifier, image, mainEntityOfPage, name, potentialAction, sameAs, url)
        self.game = game
        self.playersOnline = playersOnline
        self.serverStatus = serverStatus

    def set_game(self, game):
        self.game = game

    def get_game(self):
        return self.game

    def set_playersOnline(self, playersOnline):
        self.playersOnline = playersOnline

    def get_playersOnline(self):
        return self.playersOnline

    def set_serverStatus(self, serverStatus):
        self.serverStatus = serverStatus

    def get_serverStatus(self):
        return self.serverStatus


    def __setattr__(self, key, value_list):
        if type(value_list).__name__ == "NoneType" or key == "node_id":
            self.__dict__[key] = value_list
            return
        for value in value_list:
            str_value = type(value).__name__
            if str_value not in global_data.get_table()[key]:
                raise ValueError("非法类型!")
        self.__dict__[key] = value_list
