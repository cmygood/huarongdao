# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:07:17 2019

@author: Yuming
"""
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import random
import math
import time
from Node import Node
import Algorithm
# -*- coding: UTF-8 -*-
# encoding=gbk

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

# with open(r'D:\numb\64.txt', "r") as f:#打开64位编码转换
#     # str =''
#     imgdata = base64.b64decode(f.read())
#     file = open('zzzz.jpg', 'wb')
#     file.write(imgdata)
#     file.close()
path1= os.path.abspath('.')
a9=len(path1)+1
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False

# def post(url, data_json):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36',
#         'Content-Type': 'application/json'
#     }
#     r = requests.post(url, headers=headers, data=data_json)
#     return r.text
#
# uuid = "999d9af8-2144-4662-90e4-5c085874b623"
# url1 = 'http://47.102.118.1:8089/api/challenge/start/'+str(uuid)
# inputdata = {
#     "teamid":33,
#     "token":"e1b59e3f-5a66-4419-afea-80bfe7953a62"
# }
# data_json = json.dumps(inputdata)
# ret = json.loads(post(url1, data_json))
# data = ret["data"]
# img_base64 = data["img"]
# step = data["step"]
# swap = data["swap"]
# print(swap)
# uuid = ret["uuid"]
# img = base64.b64decode(img_base64)
# with open("zzzz.jpg", "wb") as fp:
#     fp.write(img)
#     fp.close()
# img = cv2.imread("zzzz.jpg", cv2.IMREAD_GRAYSCALE)
# for row in range(3):
#     for colum in range(3):
#         sub = img[row * 300:(row + 1) * 300, colum * 300:(colum + 1) * 300]
#         cv2.imwrite("zzz" + str(row * 3 + colum + 1) + ".jpg", sub)
# print(data)
# step = data["step"]
# print(step)
# chanceleft=ret["chanceleft"]

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



im = Image.open(r'zzzz.jpg')
img_size = im.size
m = img_size[0]    #读取图片的宽度
n = img_size[1]     #读取图片的高度
w = 300                  #设置你要裁剪的小图的宽度
h = 300                  #设置你要裁剪的小图的高度
x = 0
y = 0
a = 0
for i in range(3):         #裁剪为100张随机的小图
    for j in range(3):
        region = im.crop((300*j, 300*i, 300*j+300, 300*i+300)) #裁剪区域
        region.save("zzz" + str(a) + ".jpg")
        a = a+1



list1 = glob.glob(r'F:\华容道\*.jpg')
list2 = glob.glob(r'F:\华容道\zzz*.jpg')
lio = []
x3 = 0
x4 = 0
for i in range(325):
    x1 = compare(r'F:\华容道\zzz0.jpg', list1[i])
    if x1 != 0 :
        for j in range(i-9,i+9):
            x2 = compare(r'F:\华容道\zzz1.jpg', list1[j])
            if x2 == x1 :
                print(x2)
                x3 = 1
                # s2 = list1[j]
                # if is_number(s2[8]) == False:
                #     lio.append(int(s2[9]))
                # else:
                #     lio.append(int(s2[8]))
                break
    if x3 == 1 :
        x4 = i-8
        break

i = 0
temp1 = 0
add = 0


i = 0
j = 0

for i in range(9):
    for j in range(18):
        temp = compare1(list2[i],list1[x4+j])
        if temp != 0:
            if x2 ==list1[x4+j][7]:
                lio.append(temp)
                add = add + temp
                break
        if j == 17 :
            lio.append(0)
temp1=45-add
print(temp1)
print(lio)#输出图片序列

# 输出图片最后顺序
lio0 = []
for i in range(9):
    if i==temp1-1:
        lio0.append(0)
        continue
    lio0.append(i+1)

print(lio0)#输出要达到的东东

lio1=[]
lio2=[]
lio3=[]
lio4=[]

for i in range(0,3):
    lio1.append(lio0[i])

for i in range(3,6):
    lio2.append(lio0[i])

for i in range(6,9):
    lio3.append(lio0[i])

lio4.append(lio1)
lio4.append(lio2)
lio4.append(lio3)

# print(lio4)#目的状态的矩阵形式



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




if __name__ == '__main__':

    #
    # stepnow = step
    # swap1 = swap
    stepnow = 8
    swap1 = [1,5]
    op = ''
    # li1 = []
    # li2 = []
    # li3 = []
    # lli = []
    # # 构建初始状态、目标状态
    # for index in range(0,3):
    #     li1.append(lio[index])
    # for index in range(3,6):
    #     li2.append(lio[index])
    # for index in range(6,9):
    #     li3.append(lio[index])
    # lli.append(li1)
    # lli.append(li2)
    # lli.append(li3)
    # print(lli)#图片序列 lio 是初始列表，lio0是目的列表
    # lli=[[1, 2, 3],[4, 5, 6],[7, 9, 0]]
    # lio4=[[1, 2, 3],[4, 5, 6],[7, 0, 9]]
    # lio = forceex(lio,swap1)
    # print(lio)
    myswap = []
    lli,oper=randomstep(lio,stepnow)
    lli = getjuzhen(lli)
    startNode = Node(lli)
    endNode = Node(lio4)
    Astar = Algorithm.Astar(startNode, endNode)
    if isTransform(startNode, endNode) and Astar.start():
        Astar.showPath()
        oper+=Astar.showmotion()
        print(oper)
        print(myswap)
        # print(Astar.showPath().motion)
    else:
        lio = forceex(lio,swap1)
        print(lio)
        # print(lio)
        lli = getjuzhen(lio)
        startNode = Node(lli)
        endNode = Node(lio4)
        Astar = Algorithm.Astar(startNode, endNode)
        if isTransform(startNode, endNode) and Astar.start():
            Astar.showPath()
            oper += Astar.showmotion()
            print(oper)
            print(myswap)
        else:
            lio,s1,s2 = haveexchange(lio)
            myswap = [s1,s2]
            lli = getjuzhen(lio)
            startNode = Node(lli)
            endNode = Node(lio4)
            Astar = Algorithm.Astar(startNode, endNode)
            if isTransform(startNode, endNode) and Astar.start():
                Astar.showPath()
                oper += Astar.showmotion()
                print(oper)
                print(myswap)

    # operation = oper
    # url2 = 'http://47.102.118.1:8089/api/challenge/submit'
    # datas = {
    #     "uuid": uuid,
    #     "teamid": 33,
    #     "token": "e1b59e3f-5a66-4419-afea-80bfe7953a62",
    #     "answer": {
    #         "operations": operation,
    #         "swap": myswap
    #     }
    # }
    # data_json = json.dumps(datas)
    # ret = json.loads(post(url2, data_json))
    # for key in ret.keys():
    #     print(key + " : ", ret[key])
    #
    # print("chanceleft", chanceleft)
    #
    # #





        # print("无解")
        # Astar.showPath()
    # app = QApplication(sys.argv)
    # ex = NumberHuaRong()
    # sys.exit(app.exec_())
    # 判断是否有解
