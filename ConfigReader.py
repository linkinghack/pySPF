import json

class Configure(object):
    @staticmethod
    def readConfig(fileName="config.json"):
        return json.load(open(fileName))

