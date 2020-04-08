#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-30 14:11
from itertools import chain
import pymysql
import pprint
from electshelf_conf.mysql_conf import *

def mysql_db():

    """操作Mysql数据库"""
    db = pymysql.connect(host=mysql_host, port=int(mysql_port),
                         user=mysql_user, passwd=mysql_password,
                         db=mysql_db_name)

    cursor = db.cursor()  # 获取操作游标
    # 获取组-id
    sql = mysql_sql

    cursor.execute(sql)
    version = cursor.fetchall()
    version = list(chain.from_iterable(version))  # 定位方式  二维元组转换为一维列表
    pprint.pprint(version,indent=2)
    db.commit()
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库
    return version

mysql_db()