#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-04-01 11:29

import os
import time

import subprocess
from electshelf_conf.conf import *

def connect_devices():
    infos = os.system('adb connect {}:5555'.format(ip_224))
    if infos == 'error: device offline':
        print("设备已连接，请重启设备！！")

def subscribe():
    """
     "subscribe"=0:
     订阅关，状态改变不主动通知
     "subscribe"=1:
     订阅开，状态改变主动通知
    :return:
    """
    command = face_Focus
    return command

def face_commind():
    """
    ret=-1:故障
    ret=0:无人
    ret>0:有N人
    :return:
    """
    connect_devices()
    time.sleep(2)
    face_values = face_havepeople

    obj = subprocess.Popen("adb shell", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    infoOne = obj.communicate(("\n".join(subscribe()) + "\n").encode('utf-8'))
    print(infoOne)

    time.sleep(2)

    obj = subprocess.Popen("adb shell", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    infoTwo = obj.communicate(("\n".join(face_values) + "\n").encode('utf-8'))
    print(infoTwo)

face_commind()