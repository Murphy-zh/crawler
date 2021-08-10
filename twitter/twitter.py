#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件        :twitter.py
@说明        :按主题爬twitter
@时间        :2021/07/15 11:49:52
@作者        :zhangxy
'''
import re
import json
import requests
import pymongo
from utils import format_time,time_use,get_logger
from pymongo.errors import DuplicateKeyError
from concurrent.futures import ThreadPoolExecutor, as_completed

logger = get_logger(__file__)

class Twitter():
    def __init__(self,query) -> None:
        self.query = query
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['twitter']
        self.query_url = "https://twitter.com/search?q={}&src=typed_query".format(self.query)
        self.query_headers = {
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "accept-language": "zh-CN,zh;q=0.9",
                            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-fetch-dest": "document",
                            "sec-fetch-mode": "navigate",
                            "sec-fetch-site": "none",
                            "sec-fetch-user": "?1",
                            "upgrade-insecure-requests": "1"
                        }
        self.adaptive_url = "https://twitter.com/i/api/2/search/adaptive.json?include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media_availability=true&send_error_codes=true&simple_quoted_tweet=true&q={}&count=20&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2ChighlightedLabel".format(self.query)
        self.adaptive_headers = {
                            "accept": "*/*",
                            "accept-language": "zh-CN,zh;q=0.9",
                            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
                            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "x-csrf-token": "d856df32a73a3960098d229a6169ecfe",
                            # "x-guest-token": "1414898995533549570",
                            "x-twitter-active-user": "yes",
                            "x-twitter-client-language": "zh-cn"
                        }

    def get_gt(self):
        resp = requests.get(self.query_url,headers=self.query_headers)
        gt = re.findall(r'"gt=(141\d+); ',resp.text)
        logger.info(f'get {gt} 为空则退出')
        assert gt[0]
        return gt[0]
    
    def get_first(self):
        tmp_headers = {"x-guest-token":self.get_gt()}
        self.adaptive_headers.update(tmp_headers)
        resp = requests.get(self.adaptive_url,headers=self.adaptive_headers)
        logger.info(f'get_first_content {resp.text}')
        data = json.loads(resp.text)
        cursor = re.findall(r'"value":"(scroll:.*?)","',resp.text)
        logger.info(f'get_first_page {cursor[0]}')
        return data,cursor[0]

    def parse_content(self,data):
        globalObjects = data["globalObjects"]
        tweets = globalObjects["tweets"]
        for k,tweet in tweets.items():
            full_text = tweet["full_text"]
            user_id = tweet["user_id"]
            created_at = tweet["created_at"]
            created_time = format_time(created_at)
            users = globalObjects["users"][str(user_id)]
            items = {
                "user_id":user_id,
                "users" : users,
                "full_text" : full_text,
                "created_time" : created_time
            }
            self.insert(items)

    def insert(self,items):
        col = self.db["tw_nomal"]
        try:
            col.insert(dict(items))
            logger.success(f'{items["users"]} -> {items["user_id"]} | Insert Mongodb')
        except DuplicateKeyError:
            logger.error()(f'{items["users"]} -> {items["user_id"]} | Duplicated Data')

    def get_next(self):
        data,cursor = self.get_first()
        while cursor:
            self.parse_content(data)
            try:
                resp = requests.get(self.adaptive_url+"&cursor=" + cursor,headers=self.adaptive_headers)
                logger.info(f'get_next_content {resp.text}')
            except Exception:
                tmp_headers = {"x-guest-token": self.get_gt()}
                self.adaptive_headers.update(tmp_headers)
                resp = requests.get(self.adaptive_url + "&cursor=" + cursor, headers=self.adaptive_headers)
                logger.info(f'get_next_Exception_content {resp.text}')
            data = json.loads(resp.text)
            cursor = re.findall(r'"value":"(scroll:.*?)","',resp.text)[0]
            logger.info(f'get_next_page {self.adaptive_url+"&cursor=" + cursor}')

    @time_use
    def run(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            tasks = [executor.submit(self.get_next())]

            for future in as_completed(tasks):
                print(future.result())
        logger.info(f'time_use {time_use}')

if __name__ == '__main__':
    keywords = ["china", "Ironman"]
    for keyword in keywords:
        tw = Twitter(keyword)
        tw.get_next()
        
