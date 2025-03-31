
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
                self.allowNewUsers = (data[1][0] == "1")
            elif data[0] == "maxAccounts":
                self.maxAccounts = int(data[1])
            elif data[0] == "maxConnectedUsers":
                self.maxConnectedUsers = int(data[1])


        print("Settings: Finished reading settings file!")
        print("Allow new users: "+str(self.allowNewUsers))

