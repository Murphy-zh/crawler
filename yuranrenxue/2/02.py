import requests
import execjs
import time
from urllib import parse

def request(page,m):
    headers = {
    'User-Agent': 'yuanrenxue.project',
    'Cookie': m,
    }

    url = "http://match.yuanrenxue.com/api/match/2?page={page}".format(page=page)
    print(m,url)
    response = requests.get(url=url,headers=headers)
    print(response.text)
    return response.json()

def get_m():
    with open("02.js", 'r') as f:
        js = execjs.compile(f.read())
        m = js.call('W') 
    
    return m

if __name__ == "__main__":
    sum_list = []
    for page in range(1,6):
        m = get_m()
        print(m)
        resp = request(page,m)
        # time.sleep(1)
        values = resp.get('data')
        for i in values:
            sum_list.append(i['value'])


    average = sum(sum_list)/len(sum_list)
    print(sum_list)
    print(sum(sum_list),len(sum_list),average)


