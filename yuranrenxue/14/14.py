import execjs
import requests


def get_m(page, resp_text):
    with open("14.js", 'r',encoding="utf-8") as f:
        js = execjs.compile("var window = global\n"  + resp_text + "\n" + f.read())
        m = js.call('get_cookie', page)
        # m = js.call('sp')
    return m.replace(";path=/", "").replace("m=", "").strip()

headers = {
        'User-Agent': 'yuanrenxue.project',
    }
session = requests.Session()
for page in range(1,6):
    session.headers = headers
    url = "http://match.yuanrenxue.com/api/match/14/m"
    resp_m = session.get(url=url)
    m = get_m(page,resp_m.text)

    cookie = {
        "mz" : "TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC42NiBTYWZhcmkvNTM3LjM2LFtvYmplY3QgTmV0d29ya0luZm9ybWF0aW9uXSx0cnVlLCxbb2JqZWN0IEdlb2xvY2F0aW9uXSw4LGVzLUVTLGVzLUVTLGVzLDAsW29iamVjdCBNZWRpYUNhcGFiaWxpdGllc10sW29iamVjdCBNZWRpYVNlc3Npb25dLFtvYmplY3QgTWltZVR5cGVBcnJheV0sdHJ1ZSxbb2JqZWN0IFBlcm1pc3Npb25zXSxXaW4zMixbb2JqZWN0IFBsdWdpbkFycmF5XSxHZWNrbywyMDAzMDEwNyxbb2JqZWN0IFVzZXJBY3RpdmF0aW9uXSxNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvODcuMC40MjgwLjY2IFNhZmFyaS81MzcuMzYsR29vZ2xlIEluYy4sLFtvYmplY3QgRGVwcmVjYXRlZFN0b3JhZ2VRdW90YV0sW29iamVjdCBEZXByZWNhdGVkU3RvcmFnZVF1b3RhXSwxMDQwLDAsMCwxOTIwLDI0LDEwODAsW29iamVjdCBTY3JlZW5PcmllbnRhdGlvbl0sMjQsMTkyMCxbb2JqZWN0IERPTVN0cmluZ0xpc3RdLGZ1bmN0aW9uIGFzc2lnbigpIHsgW25hdGl2ZSBjb2RlXSB9LCxtYXRjaC55dWFucmVueHVlLmNvbSxtYXRjaC55dWFucmVueHVlLmNvbSxodHRwOi8vbWF0Y2gueXVhbnJlbnh1ZS5jb20vbWF0Y2gvMTQsaHR0cDovL21hdGNoLnl1YW5yZW54dWUuY29tLC9tYXRjaC8xNCwsaHR0cDosZnVuY3Rpb24gcmVsb2FkKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gcmVwbGFjZSgpIHsgW25hdGl2ZSBjb2RlXSB9LCxmdW5jdGlvbiB0b1N0cmluZygpIHsgW25hdGl2ZSBjb2RlXSB9LGZ1bmN0aW9uIHZhbHVlT2YoKSB7IFtuYXRpdmUgY29kZV0gfQ==", 
        "m" : m
                }
    url_api = "http://match.yuanrenxue.com/api/match/14?page={page}".format(page=page)
    session.cookies.update(cookie)
    resp = session.get(url=url_api) 
    print(resp.text)



