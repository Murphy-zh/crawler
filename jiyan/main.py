import re
import time
import json
import requests
from urllib import request
from utils.cannas_img import get_distance
from utils.track import GTrace,track


class GeetestCrack(object):
    def __init__(self):
        """
        初始化,各个请求url
        """
        self.session = requests.session()
        self.session.headers = {
            # host 要依据请求接口，api或者www,不然请求不通
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'https://www.geetest.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            }
        self.gee_demo_url = "https://www.geetest.com/demo/gt/register-slide-official?t={}"
        self.gee_type_url = "https://api.geetest.com/gettype.php?gt={gt}&callback=geetest_{ts}"
        self.gee_first_php_url = "https://api.geetest.com/get.php?gt={gt}&challenge={challenge}&lang=zh-cn&pt=0&client_type=web&w={w}&callback=geetest_{ts}"
        self.gee_first_aiax_url = "https://api.geetest.com/ajax.php?gt={gt}&challenge={challenge}&lang=zh-cn&pt=0&client_type=web&w={w}&callback=geetest_{ts}"
        self.img_url = "https://static.geetest.com/"
        self.gee_second_php_url = "https://api.geetest.com/get.php?is_next=true&type={type}&gt={gt}&challenge={challenge}&lang=zh-cn&https=true&protocol=https%3A%2F%2F&offline=false&product=float&api_server=api.geetest.com&isPC=true&autoReset=true&width=100%25&callback=geetest_{ts}"
        self.gee_second_ajax_url = "https://api.geetest.com/ajax.php?gt={gt}&challenge={challenge}&lang=zh-cn&pt=0&client_type=web&w={w}&callback=geetest_{ts}"


    def get_gt_challenge(self):
        """
        获取gt,challenge
        """
        resp = self.session.get(url=self.gee_demo_url.format(int(time.time()*1000)))
        self.gt = resp.json().get("gt")
        self.challenge = resp.json().get("challenge")
 
    def get_type(self):
        """
        中间请求
        """
        resp = self.session.get(url=self.gee_type_url.format(gt=self.gt,ts=int(time.time() * 1000)))

    def get_w1(self):
        """
        获取第一个w参数
        """
        url = "http://127.0.0.1:8898/get_w1"
        data = {
            "gt" : self.gt,
            "challenge" : self.challenge
        }
        res = requests.post(url,data=data)
        self.w1 = res.json().get("w")
        self.token_ymml = res.json().get("token_ymml")
            
    def get_first_php(self):
        resp = self.session.get(url=self.gee_first_php_url.format(gt=self.gt,challenge=self.challenge,w=self.w1,ts=int(time.time() * 1000)))
        text = re.sub(r'geetest_.*?\(',"",resp.text)
        text = text.replace(")","")
        param = json.loads(text)
        self.data = param.get("data")


    def get_w2(self):
        """
        获取第二个w参数
        """
        url = "http://127.0.0.1:8898/get_w2"
        data = {
            "gt" : self.gt,
            "challenge" : self.challenge,
            "c" : self.data.get("c"),
            "s" : self.data.get("s"),
            "token_ymml":self.token_ymml
        }
        res = requests.post(url,data=data)
        self.w2 = res.text

    def get_ajax(self):
        """
        中间请求
        """
        resp = self.session.get(url=self.gee_first_aiax_url.format(gt=self.gt,challenge=self.challenge,w=self.w2,ts=int(time.time() * 1000)))

    def get_second_php(self):
        """
        获取图片和参数
        """
        resp = self.session.get(url=self.gee_second_php_url.format(gt=self.gt,challenge=self.challenge,type="slide3",ts=int(time.time() * 1000)))
        text = re.sub(r'geetest_.*?\(',"",resp.text)
        text = text.replace(")","")
        param = json.loads(text)
        bg = self.img_url + param.get("bg")
        fullbg = self.img_url +param.get("fullbg")
        return param,bg,fullbg

    def get_w3(self,track_list,e,r,new_challenge,c,s):
        """
        获取第三个w参数
        """
        url = "http://127.0.0.1:8898/get_w3"
        data = {
            "track_list":track_list,
            "e" : e,
            "r" : r,
            "gt" : self.gt,
            "challenge" : new_challenge,
            "c" : c,
            "s" : s,
            "token_ymml":self.token_ymml
        }
        res = requests.post(url,data=data)
        return res.text

    def slide_img(self):
        """
        生成轨迹，移动滑块，生成w3
        """
        req_param,bg,fullbg = self.get_second_php()
        request.urlretrieve(bg, 'bg.png')
        request.urlretrieve(fullbg, 'fullbg.png')
        distance = get_distance("bg.png","fullbg.png")
        # new_track = track(distance-5)
        trace = GTrace()
        distance, new_track = trace.get_mouse_pos_path(distance)
        # print(distance, new_track)
        e = new_track[-1][0]
        r = new_track[-1][2]
        self.w3 = self.get_w3(new_track,e,r,req_param["challenge"],req_param["c"],req_param["s"])
        resp = self.session.get(url=self.gee_second_ajax_url.format(gt=self.gt,challenge=self.challenge,w=self.w3,ts=int(time.time() * 1000)))
        text = re.sub(r'geetest_.*?\(',"",resp.text)
        text = text.replace(")","")
        param = json.loads(text)
        print(param)
        return param
        
    def get_validate(self):
        self.get_gt_challenge()
        self.get_type()
        self.get_w1()
        self.get_first_php()
        self.get_w2()
        self.get_ajax()
        
        result = self.slide_img()
        # assert result.get("validate")
        # return result



if __name__ == '__main__':
    gee = GeetestCrack()
    gee.get_validate()
    
