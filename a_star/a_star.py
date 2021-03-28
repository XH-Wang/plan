'''
功能：A*算法
作者：Kirk
日期：2021.03.28
备注：

参考资料
1. https://blog.csdn.net/hitwhylz/article/details/23089415
2. https://github.com/AtsushiSakai/PythonRobotics
'''
import matplotlib.pyplot as plt

from math import sqrt
from math import fabs

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../com")              

from gird_map import gird_map
from trajectory import trajectory

class node:
    '''A* 搜索节点'''
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
        self.g = 0
        self.h = 0
        self.f = 0

        self.pre_node_id = -1

    def updata_cost(self, g, h):
        self.g = g
        self.h = h
        self.f = g + h

def node_value(now_node:node):
    return now_node.f

def h_euler_distance(now:node, goal:node):
    '''欧式距离启发函数'''
    h = sqrt((goal.x - now.x) ** 2 + (goal.y- now.y) ** 2)
    return h

def g_euler_distance(now:node, next:node):
    '''欧式距离代价函数'''
    g = now.g + sqrt((next.x - now.x) ** 2 + (next.y- now.y) ** 2)
    return g

def g_city_block_distance(now:node, next:node):
    '''街区距离代价函数'''
    g = now.g + fabs(next.x - now.x)  + fabs(next.y- now.y)
    return g

class a_star:
    '''A* 算法类'''
    def __init__(self, map = gird_map()):
        self.open_list = []
        self.close_list = []

        self.map = map.data
        self.start = node(map.start[0], map.start[1])
        self.goal = node(map.end[0], map.end[1])

        self.h = h_euler_distance
        self.g = g_euler_distance

    def update_expand_node(self, x, y):
        '''扩展节点更新'''
        
        # 边界保护
        if x < 0 or x >= len(self.map[0]):
            return

        if y < 0 or y >= len(self.map):
            return

        # 障碍物节点不更新
        if 0 != self.map[x][y]:
            return

        for path_node in self.close_list:
            if x == path_node.x and y == path_node.y:
                return
        
        expand_node = node(x, y)
        expand_node.pre_node_id = len(self.close_list) - 1
        expand_node.updata_cost(self.g(self.close_list[-1], expand_node),self.h(expand_node,self.goal))

        for i in range(0, len(self.open_list)):
            if x == self.open_list[i].x and y == self.open_list[i].y:
                if self.open_list[i].f > expand_node.f:
                    self.open_list[i] = expand_node
                return           
        
        self.open_list.append(expand_node)

    def expand(self, now):
        '''扩展当前节点'''
        self.update_expand_node(now.x, now.y + 1)
        self.update_expand_node(now.x - 1, now.y + 1)
        self.update_expand_node(now.x - 1, now.y)
        self.update_expand_node(now.x - 1, now.y - 1)
        self.update_expand_node(now.x, now.y - 1)
        self.update_expand_node(now.x + 1, now.y -  1)
        self.update_expand_node(now.x + 1, now.y)
        self.update_expand_node(now.x + 1, now.y + 1)

    def plan(self):
        '''执行规划'''

        # 起点初始化
        now = self.start
        now.updata_cost(self.g(now, now), self.h(now, self.goal))
        self.open_list.append(now)

        # 规划
        while 0 < len(self.open_list):
            self.open_list.sort(key = lambda  x: x.f, reverse=True)
            now = self.open_list.pop()
            self.close_list.append(now)

            if self.goal.x == now.x and self.goal.y == now.y:
                break

            self.expand(now)

        if 0 == len(self.open_list):
            print("A* 算法规划失败！")
            return trajectory()

        # 沿close list得到路径
        path = trajectory()
        path.x.append(self.close_list[-1].x)
        path.y.append(self.close_list[-1].y)
        pre_node_id = self.close_list[-1].pre_node_id

        while self.start.x != path.x[-1] or self.start.y != path.y:
            path.x.append(self.close_list[pre_node_id].x)
            path.y.append(self.close_list[pre_node_id].y) 
            pre_node_id = self.close_list[pre_node_id].pre_node_id

            if pre_node_id < 0:
                break
        
        path.x.reverse()
        path.y.reverse()

        return path

    def plot(self):
        '''绘制搜索信息'''
        x = []
        y = []

        for node in self.close_list:
            x.append(node.x)
            y.append(node.y)
        plt.plot(x, y, "xc")

        x.clear()
        y.clear()
        for node in self.open_list:
            x.append(node.x)
            y.append(node.y)
        plt.plot(x, y, "xg")


def main ():
    '''A*算法运行'''
    map = gird_map()
    #map.test_1()

    alg = a_star(map)
    path = alg.plan()

    map.plot()
    alg.plot()
    path.plot()

    plt.show()    

if __name__ == "__main__":
    main()