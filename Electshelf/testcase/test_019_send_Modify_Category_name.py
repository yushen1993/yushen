#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-04-01 10:12
from electshelf_Common_Lib.common_libs import *

'''
修改分类名称
'''

def test_019_send_Modify_Category_name():
    response = eshelfCaseLayer_addComodity()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'

    save_goods = eshelfCaseLayer_addOrUpdateCategory('test-three')    #分类名称test-two
    assert save_goods['meta']['errno'] == 0
    assert save_goods['meta']['msg'] == 'success'

    #数据变更后，检查一键更新按钮是否可用
    cheack_updata = updateData_judgeHasUpdate()
    assert cheack_updata['meta']['errno'] == 0
    assert cheack_updata['meta']['msg'] == 'success'
    if cheack_updata['result']['data']['hasUpdate'] == True: #等于true，可更新
        send_package = updateData_packUpdate()  #点击一键更新
        assert send_package['meta']['errno'] == 0
    else:
        print("无数据变更，无需更新")

    #获取模板分类名称，检查分类名称是否修改成功
    Category_name = eshelfCaseLayer_queryHomePage()
    print(Category_name['result']['data']['category']['dataList'][0]['name'])
    assert Category_name['meta']['errno'] == 0
    assert Category_name['meta']['msg'] == 'success'
    assert Category_name['result']['data']['category']['caseName'] == 'test-one'
    assert Category_name['result']['data']['category']['dataList'][0]['name'] == 'test-three'
    assert Category_name['result']['data']['category']['createBy'] == userName

    #一键更新后再次检查一键更新是否置灰
    cheack_end_updata = updateData_judgeHasUpdate()
    assert cheack_end_updata['meta']['errno'] == 0
    assert cheack_end_updata['meta']['msg'] == 'success'
    assert cheack_end_updata['result']['data']['hasUpdate'] == False