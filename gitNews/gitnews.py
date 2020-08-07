#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-08-05 10:06
from selenium import webdriver
import time
import datetime

def git_news():
    strTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    url = 'http://news.baidu.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(1)
    news_data = driver.find_elements_by_css_selector('[class="mod-tab-content"]')
    for one in news_data:
        print(one.text)
        with open('E:\yushen\data_reports\{}.txt'.format(strTime),'a',encoding='utf-8') as fp:
            fp.writelines(one.text)
    driver.quit()
    print("执行结束")