import hashlib
import base64
import requests
from fontTools.ttLib import TTFont



def get_value(name):
    # tmp_dict = {"unib538" : "4",
    #    "unie271" : "0",
    #    "unif298" : "8",
    #    "unic652" : "2",
    #    "unie354" : "1",
    #    "unie456" : "5",
    #    "unie657" : "9",
    #    "unif367" : "7",
    #    "unic584" : "3",
    #    "unif648" : "6",}
    tmp1_dict = {'f9d12372b7002b9a1522dd3dd142cf70': '8', '4119e3dc64f73251d40cf1fc0323e20f': '9', '2c0ec07331fa25dc226f1ca83561cb46': '1', 'b024173b00a3c901b6e696ba12812124': '3', '9ebca885e21990cee127d23d03acb3ac': '5', '0aef9a3385d96e7bdd1f3003669a940c': '0', '3dcfec8e26ef48730f25363da55da77a': '7', 'ec9467393c47041e0fafff7f4a2852a8': '4', 'af603543300bfc5f0e35e941d4208759': '6', '9bb92485b3e2ba4bd8a93ebbd3a0fa4e': '2'}

    font_dict = {}
    font = TTFont('{}.woff'.format(name))  # 打开当前目录的 .woff 文件
    # obj_list = font.getGlyphNames()[1:-1]
    # # 将读取出来的woff数据转为映射关系
    # cmap = font.getBestCmap()
    # font.close()
    # print(cmap)
    infos = font['glyf'].__dict__
    # print(infos["glyphs"])
    for k,v in infos["glyphs"].items():
        if k != '.notdef':
            data = font['glyf'][k].__dict__
            flags = data["flags"]
            md5_flags = hashlib.md5(flags).hexdigest()
            font_dict[k.replace("uni","")] = tmp1_dict[md5_flags]
    print(font_dict)




if __name__ == '__main__':
    get_value("2")


