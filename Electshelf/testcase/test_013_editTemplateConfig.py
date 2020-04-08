#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 17:25
from electshelf_Common_Lib.common_libs import *

def test_013_getCaseConfig():
    '''修改模板功能配置信息'''
    response = electronicShelf_editTemplateConfig(['商品', '娱乐', '餐饮', '影视','test'])
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'