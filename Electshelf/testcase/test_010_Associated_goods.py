#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 16:33
from electshelf_Common_Lib.common_libs import *

def test_010_Associated_goods():
    '''模板内现有关联商品'''
    response =commodityManage_queryCategoryCommodity()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    try:
        goods_list = [] #存储现有商品名称
        for data in response['result']['data']:
            goods_list.append(data['name'])
        # print(goods_list)
        if goods_list != None:
            assert goods_list == ['1641商品', '1204新增商品测试模板', '2020-03-17-新增测试商品']
        else:
            print("请假差商品是否被删除，现有商品信息为：{}".format(goods_list))
    except:
        print("该商品也被删除，请检查是否有该商品")
