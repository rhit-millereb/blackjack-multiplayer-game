
SETTINGS_FILE_PATH = "/home/blackjack/game_files/settings.txt"

class Settings:
    allowNewUsers: bool
    maxAccounts: int
    maxConnectedUsers: int

    def __init__(self):
        self.parseSettingsFile()

    def parseSettingsFile(self):
        try:
            doc = open(SETTINGS_FILE_PATH)
        except Exception as e:
            raise e
        
        for line in doc:
            data = line.split(":")

            if data[0] == "allowNewUsers":
                self.allowNewUsers = (data[1] == "1")
            if data[0] == "maxAccounts":


        print("New Users: "+str(self.allowNewUsers))

