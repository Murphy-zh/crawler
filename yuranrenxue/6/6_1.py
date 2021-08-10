import os
import time
import demjson
import execjs
import requests

def request(page,m,q):
    sums = 0
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Host': 'match.yuanrenxue.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    data = {
        'page': page,
        'm': m,
        # 'q': f'1-{q}|'
        'q' : q
    }

    url = "http://match.yuanrenxue.com/api/match/6?page={page}m={m}&q={q}".format(page=page,m=m,q=q)
    resp = requests.get(url=url,headers=headers, params=data)
    # response = requests.get(url, headers=headers, params=data)

    print(resp.status_code)
    print(resp.json())
    # for each in resp.json()['data']:
    #     sums += each['value'] * 24
    return resp.text

def get_param():
    # nodejs = os.popen('node 6.js')
    # para = nodejs.read()
    with open("6.js", 'r',encoding="utf8") as f:
        # os.environ["EXECJS_RUNTIME"] = "Node"
        js = execjs.compile(f.read())
        para = js.call('get_m')
    return para

if __name__ == "__main__":
    # os.environ["EXECJS_RUNTIME"] = "PhantomJS"
    # print(execjs.get().name)
    for page in range(1,6):
        # ts = int(time.time()) * 1000
        # print(ts)
        para = get_param()
        # print(para)
        m = para["m"]
        print("timestamp",para["timestamp"])
        request(page,m,para["q"])
        # time.sleep(0.3)
