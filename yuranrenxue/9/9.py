import re
import time
import execjs
import requests

headers = {
        'User-Agent': 'yuanrenxue.project',
    }

def request(page):
    url = "http://match.yuanrenxue.com/api/match/9?page={page}".format(page=page)
    resp = requests.get(url=url, headers=headers)
    return resp

def get_m(ts):
    with open("2.js", 'r') as f:
        js = execjs.compile(f.read())
        m = js.call('get_m',ts)

    return m


if __name__ == '__main__':
    url = "http://match.yuanrenxue.com/match/9"
    resp = requests.get(url=url, headers=headers)
    sessionid = re.findall(r'(sessionid=.*?);', resp.headers["Set-Cookie"])[0]
    # print(sessionid)
    ts = re.findall(r"\(decrypt,'(\d+)'\);", resp.text)[0]
    m = get_m(ts)
    headers.update({"cookie": sessionid + ";" + m})
    print(headers)
    for page in range(1,6):
        response = request(page)
        print(response.text)