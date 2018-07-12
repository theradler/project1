import requests

class darkSkyRequester(object):
    def __init__(self, key, lat, long):
        self.key = key
        self.lat = lat
        self.long = long

    def getCurrentWeather(self):
        request_string = "https://api.darksky.net/forecast/%s/%s,%s" %(self.key, self.lat, self.long)
        response = requests.get(request_string).json()
        return response["currently"]
