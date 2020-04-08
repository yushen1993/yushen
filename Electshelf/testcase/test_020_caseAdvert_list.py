#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-04-01 14:30
from electshelf_Common_Lib.common_libs import *
from electshelf_Common_Lib.down_ads_Mp4 import *

def test_020_caseAdvert_list():
    '''商家-模板广告详情'''
    response = caseAdvert_info()
    assert response['meta']['errno'] == 0
    assert response['result']['data'][0]['name'] == 'test-one-广告'
    assert response['result']['data'][0]['adUrl'] == 'http://www.baidu.com'
    adburl = response['result']['data'][0]['urls'][0]
    assert adburl == 'http://rongyi.b0.rongyi.com/system/smartService//5be53145b80a81146db071e2/6582106053008162816.mp4'
    if adburl:
        download_Mp4(adburl)    #下载视频，查看banner广告能否播放