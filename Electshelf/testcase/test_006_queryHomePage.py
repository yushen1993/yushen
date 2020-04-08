#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 14:09
from electshelf_Common_Lib.common_libs import *
from electshelf_conf.conf import *

def test_005_addOrUpdateCategory():
    '''获取模板分类列表'''
    response =eshelfCaseLayer_queryHomePage()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    assert response['result']['data']['category']['caseName'] == 'test-one'
    assert response['result']['data']['category']['createBy'] == userName