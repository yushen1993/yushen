#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-04 13:28
import  pytest
import  time as t


def add(a,b):
   try:
      return a+b
   except Exception as e:
      return e.args[0]

@pytest.mark.parametrize('a,b,result',[
      (1,1,2),
      (1.0,1.0,2.0),
      (1, 1.0, 2.0),
      (1,0,1),
      ('','',''),
      ('hi ','wuya','hi wuya'),
      (0, '', "unsupported operand type(s) for +: 'int' and 'str'"),
      (1,'hi',"unsupported operand type(s) for +: 'int' and 'str'"),
       (1.0,'wuya',"unsupported operand type(s) for +: 'float' and 'str'"),
])

def test_add(a,b,result):
   t.sleep(1)
   assert  add(a,b)==result