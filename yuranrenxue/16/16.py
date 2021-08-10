import time
import execjs
import requests


def get_m(ts):
    with open("16.js", 'r',encoding="utf-8") as f:
        js = execjs.compile(f.read())
        m = js.call('btoa',ts)
    # print(ts,m)
    return m

headers = {
        'User-Agent': 'yuanrenxue.project',
    }

url = "http://match.yuanrenxue.com/api/match/16"



for page in range(1,6):
    ts = int(time.time()) * 1000
    m = get_m(str(ts))
    params = {
    "page" : page,
    "m" : m,
    "t" : ts
    }
    resp = requests.get(url=url,headers=headers,params=params)
    print(resp.text)

