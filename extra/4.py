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



# 2.第二次访问http://www.gsxt.gov.cn/index.html更新cookie:__jsl_clearance
# resp = s.get(url)
js_pre = """
const { JSDOM } = require('jsdom');

const jsdom = new JSDOM('<!doctype html><html><body></body></html>');
const { window } = jsdom;

global.window = window;
document = {};
location = {pathname:"pathname", search:"search"};
function getCookie(func, time){
    func();
};
"""
js_str = js_pre + re.findall('<script>(.+?)</script>', resp2.text)[0]
# 删除检测浏览器相关代码, 也可以不删除, 补相关环境即可
# replace_str = re.findall(r'function go.+?var .{7,10}=.{7,10};(.+?)var .{7,10}=new Date', resp2.text)[0]
# print(replace_str)
# js_str = js_str.replace(replace_str, '')
# node里面执行setTimeout失败, 替换该函数为自定义的函数
js_str = js_str.replace('setTimeout', 'getCookie')
print(js_str)
ctx = execjs.compile(js_str)
__jsl_clearance = ctx.eval('document.cookie')
__jsl_clearance = re.findall('__jsl_clearance=(.+?);Max', __jsl_clearance)[0]
session.cookies.set('__jsl_clearance', __jsl_clearance)  # 更新cookie到session中
print('更新cookie成功:', __jsl_clearance)
