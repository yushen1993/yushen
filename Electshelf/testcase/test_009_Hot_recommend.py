#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 15:35
from electshelf_Common_Lib.common_libs import *

def test_009_Hot_recommend():
    '''爆款推荐'''
    response =eshelfCaseLayer_queryHomePage()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    assert response['result']['data']['category']['caseName'] == 'test-one'

    assert response['result']['data']['commodity']['dataList'][0]['name'] == '1204新增商品测试模板'
    assert response['result']['data']['commodity']['dataList'][1]['name'] == '1641商品'