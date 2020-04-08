#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 13:58
from electshelf_Common_Lib.common_libs import *

def test_005_addOrUpdateCategory():
    '''修改模板分类名称'''
    response =eshelfCaseLayer_addOrUpdateCategory('test-one')
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'

    #获取模板分类列表,检测该分类名称是否修改完成
    listshop = eshelfCaseLayer_queryHomePage()
    assert listshop['meta']['errno'] == 0
    assert listshop['meta']['msg'] == 'success'
    assert listshop['result']['data']['category']['caseName'] == 'test-one'