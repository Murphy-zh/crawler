import requests
import execjs
import time
from urllib import parse

def request(page,m):
    headers = {
    'Host': 'match.yuanrenxue.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'yuanrenxue.project',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    url = "http://match.yuanrenxue.com/api/match/1?page={page}&m={m}".format(page=page,m=m)

    response = requests.get(url,headers)
    print(response.text)
    return response.json()

def get_m():
    with open("01.js", 'r') as f:
        js = execjs.compile(f.read())
        m = js.call('get_m') 
    
    return m

if __name__ == "__main__":
    sum_list = []
    for page in range(1,6):
        m = get_m()
        m = m.replace('丨',parse.quote('丨'))
        resp = request(page,m)
        print(resp)
        time.sleep(1)
        values = resp.get('data')
        for i in values:
            sum_list.append(i['value'])


    average = sum(sum_list)/len(sum_list)
    print(sum_list)
    print(sum(sum_list),len(sum_list),average)


