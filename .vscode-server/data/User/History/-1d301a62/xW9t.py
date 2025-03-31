
SETTINGS_FILE_PATH = "/home/blackjack/game_files/settings.txt"

class Settings:
    allowNewUsers: bool

    def __init__(self):
        pass

    def parseSettingsFile(self):
        try:
            doc = open(SETTINGS_FILE_PATH)