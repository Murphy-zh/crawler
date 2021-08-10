import os
import time
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
        'q': q
    }

    url = "http://match.yuanrenxue.com/api/match/6?page={page}m={m}&q={q}".format(page=page, m=m, q=q)
    resp = requests.get(url=url, headers=headers, params=data)

    # print(resp.status_code)
    print(resp.json())
    for each in resp.json()['data']:
        sums += each['value'] * 24
    print(sums)
    return sums

def get_param():
    with open("6.js", 'r') as f:
        # os.environ["EXECJS_RUNTIME"] = "Node"
        js = execjs.compile(f.read())
        para = js.call('get_param')
    
    return para

if __name__ == "__main__":
    # os.environ["EXECJS_RUNTIME"] = "PhantomJS"
    # print(execjs.get().name)
    sum_vals = 0
    for page in range(1,6):
        # ts = int(time.time()) * 1000
        para = get_param()
        m = para["m"]
        q = para["q"]
        # print(m)
        # print(q)
        sums = request(page,m,q)
        # time.sleep(0.3)
        sum_vals += sums
    print(sum_vals)
