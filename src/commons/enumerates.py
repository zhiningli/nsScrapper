from enum import Enum

class Features(str, Enum):
    AMIIBO = "Amiibo Supported"
    DEMO = "Demo Available"
    DLC = "DLC Available"
    GAME_VOUCHER = "Game Voucher Eligible"
    ONLINE_PLAY = "Online Play"
    SAVE_DATA_CLOUD = "Save Data Cloud Supported"
    VOICE_CHAT = "Voice Chat Supported"

    def __str__(self):
        return str(self.value)
    
class Platforms(str, Enum):
    NINTENDO_SWITCH = "Nintendo Switch"

    def __str__(self):
        return str(self.value)
    

class Ratings(str, Enum):
    CERO = "CERP"
    PEGI = "PEGI"
    ESRB = "ESRB"


    def __str__(self):
        return str(self.value)
    

class Regions(str, Enum):
    EU = "EU"
    JP = "JP"
    NA = "NA"
    HK = "HK"

    def __str__(self):
        return str(self.value)