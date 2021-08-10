import re
import base64
import requests
from lxml import etree

headers = {
        'User-Agent': 'yuanrenxue.project',
        }
def request():

    url = "http://match.yuanrenxue.com/api/match/8_verify"
    resp = requests.get(url=url,headers=headers)
    img_reg = r'src=.*?,(.*?)" alt='
    font_reg = r'---<p>(.*?)</p>'
    fonts = re.findall(font_reg,resp.text)
    img = re.findall(img_reg,resp.text)
    # print("@@",img)
    with open("1.jpg","wb") as f:
        f.write(base64.b64decode(img[0]))
    return fonts,img

def deal_img(img):
    # 图片数据预处理，对图片处理不了解，所以都不知道要做些什么？
    # 灰度图，去噪，膨胀，腐蚀，二值化，处理背景色，处理干扰线条。
    return img

def ocr_img(img):
    # 第三方图片识别
    # 像素位置 156|165|174|456|466|476|755|766|776
    result_dict = {"图片识别结果的集合":'示例','白':'1',}
    return result_dict

def get_answer(fonts,result_dict):
    answers = []
    for font in fonts:
        answers.append(result_dict[font])

    return answers




if __name__ == '__main__':
    for page in range(1,2):
        fonts, img = request()
        img = deal_img(img)
        result_dict = ocr_img(img)
        answers = get_answer(fonts, result_dict)
        answer = "|".join(answers) + "|"
        url = "http://match.yuanrenxue.com/api/match/8?page={}&answer={}"
        data = {
            "page":page,
            "answer":answer
        }
        response = requests.get(url.format(page,answer),headers=headers,params=data)



