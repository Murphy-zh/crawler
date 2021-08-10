import time
import execjs
import requests

def request(md5_m,RM4hZBv0dDon443M,page,m,f):
    headers = {
        'User-Agent': 'yuanrenxue.project',
        'Cookie': "m={md5_m};RM4hZBv0dDon443M={RM4hZBv0dDon443M}".format(md5_m=md5_m,RM4hZBv0dDon443M=RM4hZBv0dDon443M)
        }

    url = "http://match.yuanrenxue.com/api/match/5?page={page}&m={m}&f={f}".format(page=page,m=str(m),f=str(f))
    
    resp = requests.get(url=url,headers=headers)
    print(resp.status_code,resp.text)
    return resp.text

def get_m(ts):
    with open("5.js", 'r') as f:
        js = execjs.compile(f.read())
        para = js.call('get_RM4hZBv0dDon443M',ts)
    
    return para

if __name__ == "__main__":
    ts = int(time.time() * 1000)
    f = int(time.time()) * 1000
    para = get_m(ts)
    md5_m = para["md5_m"]
    RM4hZBv0dDon443M = para["RM4hZBv0dDon443M"]
    print("md5_m : ",md5_m)
    print("RM4hZBv0dDon443M : ",RM4hZBv0dDon443M)
    for page in range(1,6):
        text = request(md5_m,RM4hZBv0dDon443M,page,ts,f)
        # print(text)