#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 17:03
from electshelf_Common_Lib.common_libs import *

def test_012_casePage_queryPage():
    '''模板样式列表'''
    response = casePage_queryPage()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'

    layoutNameList = [data['layoutName'] for data in response['result']['data']]

    if layoutNameList != None:
        assert layoutNameList == ['首页','商品列表页','其他']

    else:
        print("模板样式列表有更改：目前配置信息为{}".format(layoutNameList))