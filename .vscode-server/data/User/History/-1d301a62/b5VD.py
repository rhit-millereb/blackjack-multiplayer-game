
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
        
        for line in doc:
            data = line.split(":")

            if data[0] == "allowNewUsers":
                self.allowNewUsers = bool(data[1])

        print("New Users: "+self.allowNewUsers)

