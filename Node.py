# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:25:23 2019

@author: Yuming
"""


# 描述A*算法中的数据状态
class Node:

    def __init__(self, array2d, g=0, h=0):
        self.array2d = array2d  # 二维数组
        self.father = None  # 父节点
        self.g = g  # g值
        self.h = h  # h值

    """
    h(x)是从节点x到目标节点Sg的最优路径的估价代价,体现了问题的启发性信息,称为启发函数
    g(x)为从初始节点S0到节点x已经实际付出的代价
    """

    def setH(self, endNode):
        for x in range(0, 3):
            for y in range(0, 3):
                for m in range(0, 3):
                    for n in range(0, 3):
                        if self.array2d[x][y] == endNode.array2d[m][n] and self.array2d[x][y] != 0:
                            path = 0
                            if x == m and y != n:
                                path = abs(y - n)
                            elif y == n and x != m:
                                path = abs(x - m)
                            else:
                                path = abs(x - m) + abs(y - n)
                            self.h += path

    def getH(self):
        return self.h

    def setG(self, g):
        self.g = g

    def setFather(self, node):
        self.father = node

    def getG(self):
        return self.g