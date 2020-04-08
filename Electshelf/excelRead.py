#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-30 18:44
import xlrd

def xrld_reads():
    datas = xlrd.open_workbook('E:\Electshelf\shelfData\data.xls')
    table = datas.sheet_by_name('Sheet1')
    print(eval(table.row_values(1)[0]))
    print(type(table.row_values(1)[0]))
    print(table.row_values(1)[0])
    return table.row_values(1)[0]

xrld_reads()