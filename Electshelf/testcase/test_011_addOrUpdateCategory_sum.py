#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 16:59
from electshelf_Common_Lib.common_libs import *

def test_011_addOrUpdateCategory_sum():
    '''已关联商品'''
    response =eshelfCaseLayer_addOrUpdateCategory_sum('test-one',4,4)
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'