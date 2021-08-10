import requests

url = "https://guide-acs.m.taobao.com/gw/mtop.taobao.wsearch.appsearch/1.0/?data=%7B%22LBS%22%3A%22%7B%5C%22SG_TMCS_1H_DS%5C%22%3A%5C%22%7B%5C%5C%5C%22stores%5C%5C%5C%22%3A%5B%5D%7D%5C%22%2C%5C%22SG_TMCS_FRESH_MARKET%5C%22%3A%5C%22%7B%5C%5C%5C%22stores%5C%5C%5C%22%3A%5B%5D%7D%5C%22%2C%5C%22TB%5C%22%3A%5C%22%7B%5C%5C%5C%22stores%5C%5C%5C%22%3A%5B%7B%5C%5C%5C%22code%5C%5C%5C%22%3A%5C%5C%5C%22288190059%5C%5C%5C%22%2C%5C%5C%5C%22bizType%5C%5C%5C%22%3A%5C%5C%5C%222%5C%5C%5C%22%2C%5C%5C%5C%22type%5C%5C%5C%22%3A%5C%5C%5C%224%5C%5C%5C%22%7D%5D%7D%5C%22%2C%5C%22TMALL_MARKET_B2C%5C%22%3A%5C%22%7B%5C%5C%5C%22stores%5C%5C%5C%22%3A%5B%5D%7D%5C%22%2C%5C%22TMALL_MARKET_O2O%5C%22%3A%5C%22%7B%5C%5C%5C%22stores%5C%5C%5C%22%3A%5B%7B%5C%5C%5C%22code%5C%5C%5C%22%3A%5C%5C%5C%22567544292%5C%5C%5C%22%2C%5C%5C%5C%22bizType%5C%5C%5C%22%3A%5C%5C%5C%22DELIVERY_TIME_ONE_HOUR%5C%5C%5C%22%2C%5C%5C%5C%22type%5C%5C%5C%22%3A%5C%5C%5C%22CHOOSE_ADDR%5C%5C%5C%22%7D%2C%7B%5C%5C%5C%22code%5C%5C%5C%22%3A%5C%5C%5C%22238594195%5C%5C%5C%22%2C%5C%5C%5C%22bizType%5C%5C%5C%22%3A%5C%5C%5C%22DELIVERY_TIME_HALF_DAY%5C%5C%5C%22%2C%5C%5C%5C%22type%5C%5C%5C%22%3A%5C%5C%5C%22CHOOSE_ADDR%5C%5C%5C%22%7D%2C%7B%5C%5C%5C%22code%5C%5C%5C%22%3A%5C%5C%5C%22543259009%5C%5C%5C%22%2C%5C%5C%5C%22bizType%5C%5C%5C%22%3A%5C%5C%5C%22DELIVERY_TIME_ONE_DAY%5C%5C%5C%22%2C%5C%5C%5C%22type%5C%5C%5C%22%3A%5C%5C%5C%22CHOOSE_ADDR%5C%5C%5C%22%7D%2C%7B%5C%5C%5C%22code%5C%5C%5C%22%3A%5C%5C%5C%22404522199%5C%5C%5C%22%2C%5C%5C%5C%22bizType%5C%5C%5C%22%3A%5C%5C%5C%22DELIVERY_TIME_ONE_DAY%5C%5C%5C%22%2C%5C%5C%5C%22type%5C%5C%5C%22%3A%5C%5C%5C%22CHOOSE_ADDR%5C%5C%5C%22%7D%5D%7D%5C%22%7D%22%2C%22URL_REFERER_ORIGIN%22%3A%22https%3A%2F%2Fs.m.taobao.com%2Fh5entry%3Futparam%3D%257B%2522ranger_buckets_native%2522%253A%2522tsp2189_21618_normaluser01%2522%257D%26spm%3Da2141.1.searchbar.searchbox%26scm%3D1007.home_topbar.searchbox.d%26_navigation_params%3D%257B%2522needdismiss%2522%253A%25220%2522%252C%2522animated%2522%253A%25220%2522%252C%2522needpoptoroot%2522%253A%25220%2522%257D%22%2C%22_navigation_params%22%3A%22%7B%5C%22needdismiss%5C%22%3A%5C%220%5C%22%2C%5C%22animated%5C%22%3A%5C%220%5C%22%2C%5C%22needpoptoroot%5C%22%3A%5C%220%5C%22%7D%22%2C%22ad_type%22%3A%221.0%22%2C%22apptimestamp%22%3A%221627029355%22%2C%22areaCode%22%3A%22CN%22%2C%22brand%22%3A%22google%22%2C%22cityCode%22%3A%22110100%22%2C%22countryNum%22%3A%22156%22%2C%22device%22%3A%22Nexus+6%22%2C%22editionCode%22%3A%22CN%22%2C%22filterEmpty%22%3A%22true%22%2C%22filterUnused%22%3A%22true%22%2C%22from%22%3A%22nt_history%22%2C%22homePageVersion%22%3A%22v6%22%2C%22imei%22%3A%22355455060324396%22%2C%22imsi%22%3A%2255089Nexus62d0f%22%2C%22index%22%3A%220%22%2C%22info%22%3A%22wifi%22%2C%22itemfields%22%3A%22commentCount%2CnewDsr%22%2C%22jarvisDisable%22%3A%22true%22%2C%22latitude%22%3A%2239.97851%22%2C%22layeredSrp%22%3A%22true%22%2C%22longitude%22%3A%22116.491639%22%2C%22n%22%3A%2210%22%2C%22needTabs%22%3A%22true%22%2C%22network%22%3A%22wifi%22%2C%22new_shopstar%22%3A%22true%22%2C%22page%22%3A%223%22%2C%22q%22%3A%22%E7%BE%BD%E7%BB%92%E6%9C%8D%22%2C%22rainbow%22%3A%2214071%2C12331%2C13104%2C13837%2C14070%2C12674%2C11833%2C13276%22%2C%22referrer%22%3A%22com.taobao.taobao%22%2C%22schemaType%22%3A%22all%22%2C%22scm%22%3A%221007.home_topbar.searchbox.d%22%2C%22searchFramework%22%3A%22true%22%2C%22search_action%22%3A%22initiative%22%2C%22search_wap_mall%22%3A%22false%22%2C%22setting_on%22%3A%22imgBanners%2Cuserdoc%2Ctbcode%2Cpricerange%2Clocalshop%2CsmartTips%2CfirstCat%2Cdropbox%2Crealsale%2CinsertTexts%2Ctabs%22%2C%22showspu%22%3A%22true%22%2C%22sort%22%3A%22_coefp%22%2C%22spm%22%3A%22a2141.1.searchbar.searchbox%22%2C%22sputips%22%3A%22on%22%2C%22style%22%3A%22mid%22%2C%22subtype%22%3A%22%22%2C%22sugg%22%3A%22_0_1%22%2C%22sversion%22%3A%228.0%22%2C%22taoxianda%22%3A%22true%22%2C%22ttid%22%3A%22255200%40taobao_android_9.1.0%22%2C%22utd_id%22%3A%22YPoryXYX%2BsMDAGDz7qS%2F4yuu%22%2C%22utparam%22%3A%22%7B%5C%22ranger_buckets_native%5C%22%3A%5C%22tsp2189_21618_normaluser01%5C%22%7D%22%2C%22vm%22%3A%22nw%22%7D"
resp = requests.get(url=url)
print(resp.status_code,resp.text)

"""

"""