import requests

def request(page):
    HEADERS = {
        'Host': 'match.yuanrenxue.com',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'User-Agent': 'yuanrenxue.project',
        'Accept': '*/*',
        'Origin': 'http://match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    logo_url = "http://match.yuanrenxue.com/logo"
    # 通过session会话形式发送请求，维持会话，之后请求其他页面就不用重新发送请求头信息
    session = requests.session()
    session.headers = HEADERS  # session层面设定headers，发送的是有序字典
    r = session.post(logo_url)
    print(r.request.headers)
    print(r.cookies)

    url = "http://match.yuanrenxue.com/api/match/3?page={page}".format(page=page)
    response = session.get(url=url)
    return response.json()


if __name__ == "__main__":
    all_list = []
    for page in range(1, 6):
        resp = request(page)
        values = resp.get('data')
        for i in values:
            all_list.append(i['value'])

    print(max(all_list, key=all_list.count))
