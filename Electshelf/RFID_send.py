#-*- coding:utf-8 -*-
# @Author : yushen
import os
import time
import json
import subprocess
from electshelf_conf.conf import *

def command(values):
    """
    创建命令集合
    :param values:
    :return:
    """
    commandlist = []
    for one in values:
        commands = 'rytcptest -t 0 -d 0 --sm 1001 --dm 4 -m '+ json.dumps("{\"cmd\":\"rfid\",\"data\":{\"value\":\""+ one + "\"}}")
        commandlist.append(commands)
    return commandlist

def schreen_picture():
    '''截屏'''
    # os.system('adb connect {}:5555'.format(ip))
    os.popen('adb shell screencap -p /sdcard/yushen/{}.png'.format(time.time()))

def make_dir():
    #创建文件夹
   os.popen('adb shell mkdir /sdcard/yushen/')

def delete_dir():
    #删除文件夹
    os.popen('adb shell rm -r /sdcard/yushen/')

def Electshelf_Developer_rfid(numbers,ip):
    """
    发送命令
    :param numbers:
    :param ip:
    :return:
    """
    datatime = time.strftime("%Y-%m-%d-%H-%M-%S")
    print("开始执行时间为：{}".format(datatime))
    try:
        infos = os.system('adb connect {}:5555'.format(ip))
        if infos == 'error: device offline':
            print("设备已连接，请重启设备！！")

        # make_dir()

        os.popen(r'adb logcat *:I >E:\Electshelf\data_logs\{}_logcat.txt'.format(datatime))
        schreen_picture()
        time.sleep(2)
        for one in range(numbers):
            time.sleep(4)
            obj = subprocess.Popen("adb shell", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            info = obj.communicate(("\n".join(command(values)) + "\n").encode('utf-8'))
            print(info)
            schreen_picture()

        schreen_picture()

        time.sleep(6)
        print("开始执行pull图操作")
        os.popen('adb pull /sdcard/yushen/ E:/Electshelf/photos')
        time.sleep(6)

        # os.popen('adb disconnect')
        print(">>>>>>>>>>>>>>>>>>>>执行结束>>>>>>>>>>>>>>")

        endtime = time.strftime("%Y-%m-%d-%H-%M-%S")
        print("结束执行时间为：{}".format(endtime))

    except:
        print("请检查IP地址或者参数是否按照规定填写")
        endtime = time.strftime("%Y-%m-%d-%H-%M-%S")
        print("结束执行时间为：{}".format(endtime))

values = Rfid_values_224
number = number
ip = ip_224
Electshelf_Developer_rfid(number,ip)
# schreen_picture()