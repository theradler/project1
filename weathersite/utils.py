import requests, json

# darkskyapi = '6088666bfa2a7a4897f896605b254ffc'
# lat = '41.83'
# long = '-87.68'
# request_string = "https://api.darksky.net/forecast/%s/%s,%s" %(darkskyapi, lat, long)
# response = requests.get(request_string).json()
# print(response)

class darkSkyRequester(object):
    def __init__(self, key, lat, long):
        self.key = key
        self.lat = lat
        self.long = long

    def getCurrentWeather(self):
        request_string = "https://api.darksky.net/forecast/%s/%s/%s" %(self.key, self.lat, self.long)
        print(request_string)
        response = requests.get(request_string)
        print(response)
        return response
