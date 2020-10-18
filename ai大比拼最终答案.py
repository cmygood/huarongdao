# -*- coding: UTF-8 -*-
# encoding=gbk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from Node import Node
import Algorithm
import json
from PIL import Image
import math
import operator
from functools import reduce
import glob
import random
import os, base64
import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt
import sys
import base64
import json
import cv2
import requests
import copy
from enum import IntEnum
from tkinter import _flatten
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QMessageBox, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
from PIL import ImageChops
import tkinter as tk
import time as tm

def post(url, data_json):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36',
        'Content-Type': 'application/json'
    }
    r = requests.post(url, headers=headers, data=data_json)
    return r.text

def swap_chr (a, i, j) :
    # i = swap0[0]
    # j = swap0[1]
    if i > j:
        i, j = j, i
    # 得到ij交换后的数组
    b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
    return b


def issloved(srcLayout, destLayout):# src初始状态，dest目的状态
    # 进行判断srcLayout和destLayout逆序值是否同是奇数或偶数
    # 这是判断起始状态是否能够到达目标状态，同奇同偶时才是可达
    src=0;dest=0
    for i in range(1,9):
        fist=0
        for j in range(0,i):
          if srcLayout[j]>srcLayout[i] and srcLayout[i]!='0':# 0是false,'0'才是数字
              fist=fist+1
        src=src+fist

    for i in range(1,9):
        fist=0
        for j in range(0,i):
          if destLayout[j]>destLayout[i] and destLayout[i]!='0':
              fist=fist+1
        dest=dest+fist
    if (src%2)!=(dest%2):# 一个奇数一个偶数，不可达
        flag = 0
    else:
        flag = 1
    return flag

def solvePuzzle(srcLayout, destLayout):
   # 初始化字典
    g_dict_layouts = {}
    g_dict_layouts[srcLayout] = -1
    stack_layouts = []
    stack_layouts.append(srcLayout)# 当前状态存入列表

    bFound = False
    while len(stack_layouts) > 0:
        curLayout = stack_layouts.pop(0)#出栈
        if curLayout == destLayout:# 判断当前状态是否为目标状态
            break

        # 寻找0 的位置。
        ind_slide = curLayout.index("0")
        lst_shifts = g_dict_shifts[ind_slide]#当前可进行交换的位置集合
        for nShift in lst_shifts:
            newLayout = swap_chr(curLayout, nShift, ind_slide)

            if g_dict_layouts.get(newLayout) == None:#判断交换后的状态是否已经查询过
                g_dict_layouts[newLayout] = curLayout
                stack_layouts.append(newLayout)#存入集合

    lst_steps = []
    lst_steps.append(curLayout)
    while g_dict_layouts[curLayout] != -1:#存入路径
        curLayout = g_dict_layouts[curLayout]
        lst_steps.append(curLayout)
    lst_steps.reverse()
    return  lst_steps,len(lst_steps)

def solvePuzzle_depth(srcLayout):#src初始状态，dest目的状态
    #改为获取当前步数下的可达状态
	#初始化字典
    g_dict_layouts[srcLayout] = -1
    stack_layouts = []#所有当前状态可达的状态集合
    stack_layouts.append(srcLayout)#当前状态存入列表

    bFound = False
    curLayout = stack_layouts.pop(0)  # 出栈改为出队，cur则是当前获取到的状态
    # if curLayout == destLayout:#判断当前状态是否为目标状态
    #     break
    # 寻找0 的位置。
    ind_slide = curLayout.index("0")  # ind_slide就是0的位置
    lst_shifts = g_dict_shifts[ind_slide]  # 当前可进行交换的位置集合即0可进行交换的位置集合
    for nShift in lst_shifts:  # 0和可进行交换的所有步骤进行枚举
        newLayout = swap_chr(curLayout, nShift, ind_slide)  # 0和旁边可以进行交换的位置交换
        if g_dict_layouts.get(newLayout) == None:  # 判断交换后的状态是否已经查询过，如果没有，则存入
            g_dict_layouts[newLayout] = curLayout
            stack_layouts.append(newLayout)  # 存入集合，stack就是当前状态可达的状态
    return stack_layouts


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False


def compare(pic1,pic2):

    image1 = Image.open(pic1)
    image2 = Image.open(pic2)

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,histogram1, histogram2)))/len(histogram1))

    if differ == 0:
        s1 = pic2
        # 返回图片出自的字母
        return s1[a9]
    else:
        # 若图片不相同则返回0
        return 0
# 若图片相同，则返回小图为原字母图片的序列号
def compare1(pic1,pic2):

    image1 = Image.open(pic1)
    image2 = Image.open(pic2)

    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,histogram1, histogram2)))/len(histogram1))

    if differ == 0:
        s2 = pic2
        if is_number(s2[a9+1]) == False:
            # 若图片相同，则返回小图为原字母图片的序列号
            return int(s2[a9+2])+1
        else:
            return int(s2[a9+1])+1
    else:
        return 0

def sss(temp):
    if temp == 2:
        return 4
    if temp == 4:
        return 2
    if temp == 7:
        return 3
    if temp == 3:
        return 7
    if temp == 6:
        return 8
    if temp == 8:
        return 6
    return temp

def getStatus(Node):
    reverseOrderNumber = 0
    array2d = Node.array2d
    array = [i for item in array2d for i in item]
    array.remove(0)
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                reverseOrderNumber += 1

    return reverseOrderNumber;


def isTransform(startNode, endNode):
    start = getStatus(startNode)
    end = getStatus(endNode)

    if start % 2 != end % 2:
        return False

    return True


def haveexchange(stnode):
    stnode1 = stnode
    # for i in range(9):
    #     if stnode[i]!=0:
    #         stnode1.append(stnode[i])
    for i in range(9):
        for j in range(i,9):
            if stnode1[i] > stnode1[j] and stnode1[j] != 0:
                s1 = i
                s2 = j
                temp = stnode1[i]
                stnode1[i] = stnode1[j]
                stnode1[j] = temp
                return stnode1,s1,s2  # 返回进行有解交换过之后的列表


def forceex(stnode,step):
   opp1 = step[0]-1
   opp2 = step[1]-1
   temp = stnode[opp1]
   stnode[opp1] = stnode[opp2]
   stnode[opp2] = temp
   return stnode#返回按照要求进行强制变换的列表


def getjuzhen(stnode):
    node1 = []
    node2 = []
    node3  = []
    node4 =[]
    # 构建初始状态、目标状态
    if len(stnode)>=8:
        for index in range(0, 3):
            node1.append(stnode[index])
        for index in range(3, 6):
            node2.append(stnode[index])
        for index in range(6, 9):
            node3.append(stnode[index])
    node4.append(node1)
    node4.append(node2)
    node4.append(node3)
    return node4#列表转换为矩阵后返回

def randomstep(stnode,step):
    #进行矩阵的随机转换
    for i in range(len(stnode)):
        if stnode[i]==0:
            arr0=i
    opera = ''
    step00 = []
    if (arr0 % 3) == 0:
        step00.append(arr0+1)
        step00.append(arr0 + 2)
        if (step % 2) == 0:
            stnode1 = stnode
        else:
            stnode1 = forceex(stnode,step00)
        for j in range(step):
            if (j % 2) == 0:
                opera += 'd'
            else:
                opera += 'a'
    else:
        step00.append(arr0+1)
        step00.append(arr0)
        if (step % 2) == 0:
            stnode1 = stnode
        else:
            stnode1 = forceex(stnode,step00)
        for j in range(step):
            if (j % 2) == 0:
                opera += 'a'
            else:
                opera += 'd'
    return stnode1,opera






if __name__ == "__main__":
    uuid = ""  # 输入输入题目的uuid！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    g_dict_layouts = {}
    # 每个位置可交换的位置集合
    g_dict_shifts = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                     3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
                     6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
    path1 = os.path.abspath('.')
    print("path1:",path1)
    a9 = len(path1) + 1
    str_path1=[path1,"\*.jpg"]
    str_path2=[path1,"\zzz*.jpg"]
    str_path=""
    str_path0=""
    str_path=str_path.join(str_path1)
    str_path0=str_path0.join(str_path2)
    print("str_path:",str_path)
    print("str_path0:", str_path0)


    url1 = 'http://47.102.118.1:8089/api/challenge/start/'+str(uuid) #获取赛题信息的url
    inputdata = {
        "teamid":33,
        "token":"e1b59e3f-5a66-4419-afea-80bfe7953a62"
    }
    data_json = json.dumps(inputdata)
    ret = json.loads(post(url1, data_json)) # 获取赛题信息，ret为post后的返回值转化的字典
    data = ret["data"] # 获取该题data
    img_base64 = data["img"] # 获取图片64编码
    step = data["step"] # 获取调换的步数
    swap = data["swap"] # 获取调换的列表值
    print(swap)
    uuid2 = ret["uuid"] # 获取题目的返回uuid值
    img = base64.b64decode(img_base64) # 将64位编码转化为图片并保存在zzzz.jpg
    with open("zzzz.jpg", "wb") as fp:
        fp.write(img)
        fp.close()
    img = cv2.imread("zzzz.jpg", cv2.IMREAD_GRAYSCALE) # 将赛题图片切割为3*3小图
    for row in range(3):
        for colum in range(3):
            sub = img[row * 300:(row + 1) * 300, colum * 300:(colum + 1) * 300]
            cv2.imwrite("zzz" + str(row * 3 + colum + 1) + ".jpg", sub)
    print(data)
    step = data["step"]
    print(step)
    chanceleft=ret["chanceleft"]
    print('chanceleft:',chanceleft)
# 测试数据输入格式

    im = Image.open(r'zzzz.jpg')
    img_size = im.size
    m = img_size[0]  # 读取图片的宽度
    n = img_size[1]  # 读取图片的高度
    w = 300  # 设置你要裁剪的小图的宽度
    h = 300  # 设置你要裁剪的小图的高度
    x = 0
    y = 0
    a = 0
    for i in range(3):  # 裁剪为100张随机的小图
        for j in range(3):
            region = im.crop((300 * j, 300 * i, 300 * j + 300, 300 * i + 300))  # 裁剪区域
            region.save("zzz" + str(a) + ".jpg")
            a = a + 1

    list1 = glob.glob(str_path)
    list2 = glob.glob(str_path0)
    lio = []
    x3 = 0
    x4 = 0
    for i in range(325):
        x1 = compare(list2[0], list1[i])
        if x1 != 0:
            for j in range(i - 9, i + 9):
                x2 = compare(list2[1], list1[j])
                if x2 == x1:
                    print(x2)
                    x3 = 1
                    break
        if x3 == 1:
            x4 = i - 8
            if x4 < 0:
                x4 = 0
            break

    i = 0
    temp1 = 0
    add = 0

    for i in range(9):
        for j in range(18):
            if x4 + j < 325:
                temp = compare1(list2[i], list1[x4 + j])
                if temp != 0:
                    if x2 == list1[x4 + j][a9]:
                        temp = sss(temp)
                        lio.append(temp)
                        add = add + temp
                        break
            if j == 17:
                lio.append(0)
    temp1 = 45 - add # 图片缺失序列
    print(temp1)

    print(lio)  # 输出图片序列

    # 输出图片最后顺序
    lio0 = []
    for i in range(9):
        if i == temp1 - 1:
            lio0.append(0)
            continue
        lio0.append(i + 1)

    print(lio0)  # 输出要达到的东东

    lio1 = []
    lio2 = []
    lio3 = []
    lio4 = []

    for i in range(0, 3):
        lio1.append(lio0[i])

    for i in range(3, 6):
        lio2.append(lio0[i])

    for i in range(6, 9):
        lio3.append(lio0[i])

    lio4.append(lio1)
    lio4.append(lio2)
    lio4.append(lio3)

    # print(lio4)#目的状态的矩阵形式

    stepnow = step# 步数############
    swap =swap# 强制交换￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥############
    anflag = temp1# 缺了第几个##########
    print('temp:',temp1)
    strlio=""
    strlio0=""
    lio = [str(x) for x in lio]
    strlio = strlio.join(lio) # lio列表转化为字符串
    lio0 = [str(x) for x in lio0]
    strlio0 = strlio0.join(lio0) # lio0列表转化为字符串
    srcLayout  = strlio# 这是初始序列##############3
    print(srcLayout)
    destLayout = strlio0# 这是目的序列########3
    lst_stack= solvePuzzle_depth(srcLayout)# 获得当前状态的可达状态
    # print('-------------------')
    lst = lst_stack# 当前状态的所有可达状态的集合
    for index in range(stepnow-1):
        lsttemp = lst# 暂时存储当前所有可达状态
        lst = []
        for i in range(len(lsttemp)):
            lsttemp1 = lsttemp[i]#遍历得到当前集合中的一个序列
            lsttemp2 = solvePuzzle_depth(lsttemp1)#获得当前序列的可达状态
            lst+=lsttemp2
    # print(lst)#输出step步数后所有可达状态
    changelst = []#经过强制交换之后的可达序列
    for index in range(len(lst)):
        temp = lst[index]#当前index下lst的一个可达序列
        s1 = swap[0]-1
        s2 = swap[1]-1
        btemp = swap_chr(temp,s1,s2)
        changelst.append(btemp)#将交换之后的存入changelst集合
    # print(changelst)#输出changelst集合
    # print(btemp)
    # print(' ')
    myswap = []
    # final = []#final1就是最终与表匹配的列表可解的
    # final2 = []#不可解的
    # for index in range(len(changelst)):
    #     flag = issloved(changelst[index],destLayout)
    #     # print(flag)
    #     if flag==1:
    #         final.append(changelst[index])
    #     else:
    #         atemp = swap_chr(changelst[index],1,3)#可解交换
    #         final2.append(atemp)#加入表中
    # flage1 = '106435782'
    # fl = issloved(flage1,destLayout)
    # print('是否可解：',fl)

    # for index in range(len(final1)):
    #     print(final1[index])
    #     print('  ')
    # print('------------------')
    # print('无解交换过之后的列表')
    # print('    ')
    # for index in range(len(final2)):
    #     print(final2[index])
    #     print('   ')
    if(anflag==9):
        f2 = open(r'D:\answer\ans9.json', "r")
    elif (anflag == 8):
        f2 = open(r'D:\answer\ans8.json', "r")
    elif (anflag == 7):
        f2 = open(r'D:\answer\ans7.json', "r")
    elif (anflag == 6):
        f2 = open(r'D:\answer\ans6.json', "r")
    elif (anflag == 5):
        f2 = open(r'D:\answer\ans5.json', "r")
    elif (anflag == 4):
        f2 = open(r'D:\answer\ans4.json', "r")
    elif (anflag == 3):
        f2 = open(r'D:\answer\ans3.json', "r")
    elif (anflag == 2):
        f2 = open(r'D:\answer\ans2.json', "r")
    else:
        f2 = open(r'D:\answer\ans1.json', "r")
    dict2 = json.load(f2)  # 访问表
    # print(dict2)
    dictpanduan = changelst[0]#获取键，随时更新
    if issloved(dictpanduan,destLayout)==1:
        after = dict2[dictpanduan]  # 返回键值
        myswap = []
    else:
        atemp = swap_chr(changelst[0], 1, 3)  # 可解交换
        after = dict2[atemp]
        myswap=[2,4]
    panduan = 0 #用于跟踪是哪一个元素，计算之前的步数
    for index in range(len(changelst)):
        if issloved(changelst[index], destLayout) == 1:
            after1 = dict2[changelst[index]]  # 返回键值
            myswap1 = []
        else:
            atemp = swap_chr(changelst[index], 1, 3)  # 可解交换
            after1 = dict2[atemp]
            myswap1 = [2, 4]
        # print(after1)
        if len(after1)<len(after):
            after = after1
            panduan = index
            myswap = myswap1
    print(after)
    # print(final[panduan])
    print(changelst[panduan])

    # print(panduan)
    # print(lst[panduan])
    llllll = lst[panduan]###########################
    motion = ''
    lst_steps,length= solvePuzzle(srcLayout, llllll)
    # print(length)
    for nIndex in range(len(lst_steps)):
        lst_step1 = lst_steps[nIndex]
        # print(lst_step1)
        if nIndex<len(lst_steps)-1:
           lst_step2 = lst_steps[nIndex+1]
           for x in range(len(lst_step1)):
               if lst_step1[x]=='0':
                    # motion='fff'
                    if(x%3)-1>=0 and lst_step2[x-1]=='0':
                        motion = motion + 'a'
                    if (x % 3) + 1 < 3 and lst_step2[x + 1] == '0':
                        motion = motion + 'd'
                    if x>=3  and lst_step2[x - 3] == '0':
                            motion = motion + 'w'
                    if x<=5 and lst_step2[x + 3] == '0':
                            motion = motion + 's'

        print('------------------')
        print("step #" + str(nIndex + 1))
        print(lst_steps[nIndex][:3])
        print(lst_steps[nIndex][3:6])
        print(lst_steps[nIndex][6:])
        print('-----------------')
    print(motion)
    operation = ''
    operation+=motion
    operation+=after#operation为操作序列，myswap为自己调换的
    print('=============')
    print('operation:',operation)
    print('myswap:',myswap)
    # ddd = '103524786'
    # ppp = dict2[dictflag]

    url2 = 'http://47.102.118.1:8089/api/challenge/submit'
    datas = {
        "uuid": uuid2,
        "teamid": 33,
        "token": "e1b59e3f-5a66-4419-afea-80bfe7953a62",
        "answer": {
            "operations": operation,
            "swap": myswap
        }
    }
    data_json = json.dumps(datas)
    ret = json.loads(post(url2, data_json))
    for key in ret.keys():
        print(key + " : ", ret[key])

    print("chanceleft", chanceleft)
