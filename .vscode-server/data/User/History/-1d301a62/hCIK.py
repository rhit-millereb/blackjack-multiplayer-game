
class Settings:
    allowNewUsers: bool

    def __init__(self):
        pass

    def parseSettingsFile(self):
        try:
            doc = open("../")