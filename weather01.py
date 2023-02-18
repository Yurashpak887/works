import json
from pprint import pprint
from urllib.request import urlopen
import err

ENDPOINT_URL = 'https://api.open-meteo.com/v1/forecast?{params}'
def req_url (**kwargs):
    params ='&'.join([f'{k}={v}' for k, v in kwargs.items()])
    return ENDPOINT_URL.format(params=params)


def get_curtemp(response):
    '''get current temperature from parser json'''

    current = response["current_weather"]
    current_temp = float(current["temperature"])
    return current_temp


def make_request(**kwargs):
    url = req_url(**kwargs)
    print(url)
    print()

    response = urlopen(url)
    data = response.read()
    print(data)
    print()
    data = data.decode('utf-8')

    res = json.loads(data)
    print(res)
    return res

def request_curtemp(latitude, longitude):

    resp = make_request(latitude=latitude, longitude=longitude, current_weather='true')
    temp = get_curtemp(resp)
    return temp






if __name__ == '__main__':
    indata = r'''{"latitude=50.56&longitude=30.52&current_weather=true"}'''

    params = dict(latitude=50.56, longitude=30.52, current_weather='true' )
    r = req_url(**params)
    expected_url = ('https://api.open-meteo.com/v1/forecast?'
                 'latitude=50.56&longitude=30.52'
                 '&current_weather=true')




#latitude, longitude = 50.4375, 30.5
class City:

    def __init__(self, city, latitude1, longitude1):
        self.city = city
        self.latitude1 = latitude1
        self.longitude1 = longitude1

        if type(city) != str:
            raise err.NameCityErr()

    def __repr__(self):
        print(self.city, self.latitude1, self.longitude1)


class Weather(City):
    def req_weather(self):
        city1 = self.city
        try:
            temp = request_curtemp(self.latitude1, self.longitude1)
            print(f'Currently weather in {city1} is {temp} C ')
        except:
            raise err.CoordErr()



a = Weather("Lviv", 49.847691, 24.025244)

a.req_weather()

