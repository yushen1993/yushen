#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-08-05 13:25
import allure

@allure.testcase('持续集成-测试断言')
def test_08_demo():
    assert 3+5==8
    print("测试通过")
if __name__ == '__main__':
    test_08_demo()