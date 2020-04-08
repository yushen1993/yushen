#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 15:24
from electshelf_Common_Lib.common_libs import *

def test_008_addOrUpdateCategory():
    '''检测一键更新'''
    response = updateData_judgeHasUpdate()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    assert response['result']['data']['hasUpdate'] == True
    assert response['success'] == True