import hashlib
import base64
import requests
from io import BytesIO
# from xml.dom.minidom import parse
from fontTools.ttLib import TTFont


def request(page):
    headers = {
        'User-Agent': 'yuanrenxue.project',
        }

    url = "http://match.yuanrenxue.com/api/match/7?page={page}".format(page=page)
    resp = requests.get(url=url,headers=headers)
    return resp.json()

def get_value(woff_data):
    # font_dict = {}
    # with open('{}.woff'.format(name), 'wb') as f:
    #     f.write(base64.b64decode(woff_data))
    # font = TTFont('{}.woff'.format(name))  # 打开当前目录的 movie.woff 文件
    # font.saveXML('{}.xml'.format(name))  # 另存为 movie.xml
    #
    # # 读取文件
    # dom = parse('{}.xml'.format(name))
    # # 获取文档元素对象
    # data = dom.documentElement
    # # 获取 post
    # psNames = data.getElementsByTagName('psName')
    # x = 1
    # for psName in psNames:
    #     key = psName.getAttribute('name').replace("uni","&#x")
    #     font_dict[key] = x
    #     x +=1
    #     if x == 11:
    #         font_dict[key] = 0
    # print(font_dict)
    # return font_dict

    tmp1_dict = {'f9d12372b7002b9a1522dd3dd142cf70': '8', '4119e3dc64f73251d40cf1fc0323e20f': '9',
                 '2c0ec07331fa25dc226f1ca83561cb46': '1', 'b024173b00a3c901b6e696ba12812124': '3',
                 '9ebca885e21990cee127d23d03acb3ac': '5', '0aef9a3385d96e7bdd1f3003669a940c': '0',
                 '3dcfec8e26ef48730f25363da55da77a': '7', 'ec9467393c47041e0fafff7f4a2852a8': '4',
                 'af603543300bfc5f0e35e941d4208759': '6', '9bb92485b3e2ba4bd8a93ebbd3a0fa4e': '2'}

    font_dict = {}
    font = TTFont(BytesIO(base64.b64decode(woff_data)))  # 打开当前目录的 movie.woff 文件
    infos = font['glyf'].__dict__
    # print(infos["glyphs"])
    for k, v in infos["glyphs"].items():
        if k != '.notdef':
            data = font['glyf'][k].__dict__
            flags = data["flags"]
            md5_flags = hashlib.md5(flags).hexdigest()
            font_dict[k.replace("uni","&#x")] = tmp1_dict[md5_flags]
    print(font_dict)
    return font_dict


if __name__ == '__main__':
    sum_values = []
    for page in range(1,6):
        json_data = request(page=page)
        woff_data = json_data.get("woff")
        font_dict = get_value(woff_data)
        value_data = json_data.get("data")
        print(page,value_data)
        for data in value_data:
            values = data["value"].split()
            value_real = ""
            for value in values:
                value_real += str(font_dict[value])
            # print(value_real)
            sum_values.append(value_real)
    print(len(sum_values),max(sum_values),sum_values.index(max(sum_values)),sum_values)





"""
[{'value': '&#xb745 &#xf461 &#xb745 &#xa319 '}, 
 {'value': '&#xc932 &#xe951 &#xc936 &#xb742 '}, 
 {'value': '&#xb745 &#xf453 &#xc932 &#xf831 '}, 
 {'value': '&#xf831 &#xc932 &#xc932 &#xe951 '}, 
 {'value': '&#xa549 &#xe951 &#xb745 &#xa549 '}, 
 {'value': '&#xf831 &#xf831 &#xf453 &#xf831 '}, 
 {'value': '&#xf461 &#xb742 &#xf453 &#xe951 '}, 
 {'value': '&#xf831 &#xc936 &#xe951 &#xe951 '}, 
 {'value': '&#xc936 &#xc932 &#xe951 &#xe951 '}, 
 {'value': '&#xa549 &#xc936 &#xa549 &#xf831 '}]

"""