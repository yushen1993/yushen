#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-04-01 14:39
import requests
import time

def download_Mp4(mp4_url):
    resp = requests.get(mp4_url, stream=True)
    mp4_info = resp.content
    with open('E:\Electshelf\photos\{}.mp4'.format(str(time.time())[-4:]),'wb') as fp:
        fp.write(mp4_info)