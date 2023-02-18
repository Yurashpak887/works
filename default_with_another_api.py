import json
from statistics import mean
import numpy as np
from pprint import pprint
from urllib.request import urlopen
ENDPOINT_URL = 'https://api.tomorrow.io/v4/timelines?{params}&fields=temperature&timesteps=1h&units=metric&apikey=tCthW1X8N3BThujxVpu9QBDiS1SQqIQm'
def req_url (**kwargs):
    params ='&'.join([f'{k}={v}' for k, v in kwargs.items()])
    return ENDPOINT_URL.format(params=params)


def get_curtemp(response):


    current = response["data"]

    current_temp2 = current["timelines"]
    print("Показник темпаратури в заданому місті за годину:")
    for i in current_temp2:
        a=i['intervals']
        for i1 in a:
            a1=i1["values"]
            a2 = int(a1["temperature"])
            print(a2)



    return a2


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

def request_curtemp(location):

    resp = make_request(location=loc1)
    temp = get_curtemp(resp)
    return temp
if __name__ == '__main__':
    loc = 49.847691, 24.025244


    loc1 = (",".join(str(item) for item in loc))
    params = {"location":loc1}
    r = req_url(**params)
    make_request(**params)
    request_curtemp("Lviv")
