#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 14:22
from electshelf_Common_Lib.common_libs import *

def test_007_addOrUpdateCategory():
    '''删除分类下商品'''
    #删除商品前先列出分类商品，获取caseid
    response =commodityManage_queryCategoryCommodity()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    try:
        assert response[ 'result']['data'][0]['name'] == '1203商品'
        assert response[ 'result']['data'][0]['shopId'] == '5c2c2adbb80a8117ea575ea2'
        assert response[ 'result']['data'][0]['shopName'] == '语过添晴'
        assert response[ 'result']['data'][0]['sourceList'] != None
    except:
        print("该商品也被删除，请检查是否有该商品")

    getShop_caseID = response[ 'result']['data'][0]['id']

    if getShop_caseID != None:
        deleteCommodity = eshelfCaseLayer_deleteCommodity(int(getShop_caseID))
        assert deleteCommodity['meta']['errno'] == 0
        assert deleteCommodity['meta']['msg'] == 'success'

    # 删除完成以后，再次调用列出商品，检查是否删除
    listShop = commodityManage_queryCategoryCommodity()
    assert listShop['meta']['errno'] == 0
    assert listShop['meta']['msg'] == 'success'
    assert listShop['result']['data'][0]['name'] != '1203商品'