
SETTINGS_FILE_PATH = "/home/blackjack/game_files/settings.txt"

class Settings:
    allowNewUsers: bool

    def __init__(self):
        pass

    def parseSettingsFile(self):
        try:
            doc = open(SETTINGS_FILE_PATH)
        except Exception as e:
            raise e
        
        i = 0
        for line in doc:
            data = line.split(":")

            i+=1