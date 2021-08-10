import requests
import execjs
import re
import os

session = requests.session()
headers_pre = {

'Host':	'www.gsxt.gov.cn',
'Upgrade-Insecure-Requests'	:"1",
'User-Agent':	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
'Accept'	:'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Referer':	'http://www.gsxt.gov.cn/index.html',
'Accept-Encoding'	:'gzip, deflate',
'Accept-Language':	'zh-CN,zh;q=0.9',
}
url = "http://www.gsxt.gov.cn/index.html"

resp1 = session.get(url=url,headers=headers_pre)
data1 = resp1.text.replace("<script>document.cookie=","").replace("</script>","").replace(";location.href=location.pathname+location.search","")
# print(data1)
# print(resp1.headers["Set-Cookie"])
jsluid_h = resp1.headers["Set-Cookie"].replace("max-age=31536000; path=/; HttpOnly","")
default = execjs.get()
cookie = default.eval(data1)
cookie_pattern = cookie.replace("max-age=3600;path=/","")

headers_pre.update({
    "cookie" : jsluid_h + cookie_pattern
})

# print(headers_pre)
resp2 = session.get(url=resp1.url,headers=headers_pre)

js2 = resp2.text.replace("<script>","").replace("</script>","")
print(js2)

# headers_tool = {
# 'Host': 'tool.yuanrenxue.com',
# 'Accept': 'application/json, text/javascript, */*; q=0.01',
# 'X-Requested-With': 'XMLHttpRequest',
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
# 'Accept-Encoding': 'gzip, deflate',
# }
# tool_ob = "http://tool.yuanrenxue.com/api/ob2"
# param = {
#     "m" : str(js2)
# }
# resp3 = requests.post(url=tool_ob,headers=headers_tool,data=param)
# data2 = resp3.json().get("result")
# # print(data2)
# # js = execjs.compile(data2)
# # doco= js.call('go', param)
# fun_go = re.findall(r"(if \(.*?\(\)\) \{[\s\S]*return;[\s\S]*?\})",data2)[0]
# # print(fun_go)
# data3 = data2.replace(fun_go,"")
# print(data3)
#
# os.environ["EXECJS_RUNTIME"] = "PhantomJS"
# js = execjs.compile(data3)
# doco= js.call('go', param)
# print(doco)
#
#
#
#
