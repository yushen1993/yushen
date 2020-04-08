#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 13:47
from electshelf_Common_Lib.common_libs import *

def test_004_addComodity():
    '''添加商品'''
    response =eshelfCaseLayer_addComodity()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'

    #列出商品检查该商品是否存在
    listshop = commodityManage_queryCategoryCommodity()
    assert listshop['meta']['errno'] == 0
    assert listshop['meta']['msg'] == 'success'
    assert listshop['result']['data'][0]['name'] == '1203商品'
    assert listshop['result']['data'][0]['shopId'] == '5c2c2adbb80a8117ea575ea2'
    assert listshop['result']['data'][0]['shopName'] == '语过添晴'
    assert listshop['result']['data'][0]['sourceList'] != None