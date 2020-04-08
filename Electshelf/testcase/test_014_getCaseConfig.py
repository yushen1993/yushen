#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 17:15
from electshelf_Common_Lib.common_libs import *

def test_014_getCaseConfig():
    '''获取模板功能配置信息'''
    response = electronicShelf_getCaseConfig()
    assert response['result']['data']['configJson']['keywordList'] == keywordList
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'