#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 10:13
from electshelf_Common_Lib.common_libs import *

def test_003_ueryCategoryCommodity():
    '''列出商品'''
    response =commodityManage_queryCategoryCommodity()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    try:
        assert response[ 'result']['data'][0]['name'] == '1203商品'
        assert response[ 'result']['data'][0]['shopId'] == '5c2c2adbb80a8117ea575ea2'
        assert response[ 'result']['data'][0]['shopName'] == '语过添晴'
        assert response[ 'result']['data'][0]['sourceList'] != None
    except:
        print("该商品也被伤处，请检查是否有该商品")