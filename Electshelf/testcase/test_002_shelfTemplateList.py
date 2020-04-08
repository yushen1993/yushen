#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-30 17:18
from electshelf_Common_Lib.common_libs import *
from electshelf_conf.conf import *

def test_002_merchantTemplate_shelfTemplateList():
    '''测试 商家-电子货架模板配置列表'''
    cm = merchantTemplate_shelfTemplateList()
    #效验关键字段对应的值是否否和预期
    assert cm['meta']['errno'] == 0
    assert cm['meta']['msg'] == 'success'
    response = cm['result'][ 'data']
    assert response[0]['mallId'] == mallId
    assert response[1]['mallId'] == mallId
    assert response[0]['moduleType'] == 2   #1.炫酷版 2.标准版
    assert response[0]['name'] ==  '标准版'

    #判断返回字段是否完整
    body_dict = response[0]
    key_List = [key for key in body_dict]
    assert key_List == ['mallId','templateId','moduleType','name','type','preview','style']

    #判断返回字段对应的值是否和预期相等
    dataList = [data['name'] for data in response]
    try:
        assert dataList == ['标准版','炫酷版']
    except:
        print("列表元素有变化，请检查{}".format(response))
    print(dataList)