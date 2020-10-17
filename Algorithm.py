# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:25:45 2019

@author: Yuming
"""
from Node import Node
import copy


def showMap(node):
    # print("代价:", node.g)
    # print("启发性信息:", node.h)
    # print("估价函数:", node.g + node.h)
    for x in range(0, 3):
        for y in range(0, 3):
            print(node.array2d[x][y], end='')
        print(" ")
    print("--------")
    return;


def move(array2d, srcX, srcY, drcX, drcY):
    temp = array2d[srcX][srcY]
    array2d[srcX][srcY] = array2d[drcX][drcY]
    array2d[drcX][drcY] = temp
    return array2d;


class Astar:

    def __init__(self, startNode, endNode):
        """
        startNode:  寻路起点
        endNode:    寻路终点
        """
        # 开放列列表
        self.openList = []
        # 封闭列表
        self.closeList = []
        # 起点
        self.startNode = startNode
        # 终点
        self.endNode = endNode
        # 当前处理的节点
        self.currentNode = startNode
        # 最后生成的路径
        self.pathlist = []
        self.listpath = []
        # step步
        self.step = 0

    def getMinFNode(self):
        """
        获得openlist中f(x)最小的节点
        """
        nodeTemp = self.openList[0]
        for node in self.openList:
            if node.g + node.h < nodeTemp.g + nodeTemp.h:
                nodeTemp = node
        return nodeTemp

    def nodeInOpenlist(self, node):
        """
        判断结点是否在开放列表
        """
        for nodeTmp in self.openList:
            if nodeTmp.array2d == node.array2d:
                return True
        return False

    def nodeInCloselist(self, node):
        """
        判断结点是否在封闭列表
        """
        for nodeTmp in self.closeList:
            if nodeTmp.array2d == node.array2d:
                return True
        return False

    def endNodeInOpenList(self):
        """
        目标状态是否在开放列表中
        """
        for nodeTmp in self.openList:
            if nodeTmp.array2d == self.endNode.array2d:
                return True
        return False

    def getNodeFromOpenList(self, node):
        """
        返回输入状态在开放列表的代价，启发性信息
        """
        for nodeTmp in self.openList:
            if nodeTmp.array2d == node.array2d:
                return nodeTmp
        return None

    def searchOneNode(self, node):
        """
        将移动后的状态放入开放列表
        """
        # 忽略封闭列表
        if self.nodeInCloselist(node):
            return
            # G值计算
        gTemp = self.step

        # 如果不在openList中，就加入openlist
        if self.nodeInOpenlist(node) == False:
            node.setG(gTemp)
            # H值计算
            node.setH(self.endNode);
            self.openList.append(node)
            node.father = self.currentNode
        # 如果在openList中，判断currentNode到移动后结点的G是否更小
        # 如果更小，就重新计算g值，并且改变父结点
        else:
            nodeTmp = self.getNodeFromOpenList(node)
            if self.currentNode.g + gTemp < nodeTmp.g:
                nodeTmp.g = self.currentNode.g + gTemp
                nodeTmp.father = self.currentNode
        return;

    def searchNear(self):
        """
        搜索下一个可以动作的数码
        找到0所在的位置并以此进行交换
        """
        flag = False
        for x in range(0, 3):
            for y in range(0, 3):
                if self.currentNode.array2d[x][y] == 0:
                    flag = True
                    break;
            if flag == True:
                break;

        self.step += 1
        # 深复制，不改变原状态
        # 判断0位置
        if x - 1 >= 0:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x - 1, y)
            self.searchOneNode(Node(arrayTemp));
        if x + 1 < 3:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x + 1, y)
            self.searchOneNode(Node(arrayTemp));
        if y - 1 >= 0:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x, y - 1)
            self.searchOneNode(Node(arrayTemp));
        if y + 1 < 3:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x, y + 1)
            self.searchOneNode(Node(arrayTemp));

        return;

    def start(self):
        '''''
        开始寻路
        '''
        # 将初始节点加入开放列表
        self.startNode.setH(self.endNode);
        self.startNode.setG(self.step);
        self.openList.append(self.startNode)

        while True:
            # 获取当前开放列表里F值最小的节点
            self.currentNode = self.getMinFNode()
            # 将结点放入到已经闭合列表
            self.closeList.append(self.currentNode)
            # 将结点从开放列表中移除
            self.openList.remove(self.currentNode)
            # 代价+1
            self.step = self.currentNode.getG();
            # 搜索当前结点可走的路径
            self.searchNear();

            # 检验是否结束
            if self.endNodeInOpenList():
                nodeTmp = self.getNodeFromOpenList(self.endNode)
                while True:
                    self.pathlist.append(nodeTmp);
                    if nodeTmp.father != None:
                        nodeTmp = nodeTmp.father
                    else:
                        return True;
            elif len(self.openList) == 0:
                return False;
            elif self.step > 30:
                return False;

        return True

    def showPath(self):
        global motion
        motion = ""
        for node in self.pathlist[::-1]:
            self.listpath.append(node)
        for index in range(len(self.listpath)):
            node1 = self.listpath[index]
            if index < len(self.listpath)-1:
                node2 = self.listpath[index+1]
                for x in range(0,3):
                    for y in range(0,3):
                        if node1.array2d[x][y]==0:
                            if x-1>=0 and node2.array2d[x-1][y]==0:
                                motion = motion+'w'
                            if x+1<3 and node2.array2d[x+1][y]==0:
                                motion = motion+'s'
                            if y-1>=0 and node2.array2d[x][y-1]==0:
                                motion = motion+'a'
                            if y+1<3 and node2.array2d[x][y+1]==0:
                                motion = motion+'d'
            # showMap(node1)

    def showmotion(self):
        # print(motion)
        return motion



