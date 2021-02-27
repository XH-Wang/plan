import matplotlib.pyplot as plt #约定俗成的写法plt

from numpy import *

def draw_map(map):
    '''
    绘制地图
    ''' 
    for i in map:
        for j in i:
            if 0 != j:   #栅格地图上obstacle为障碍物标识
                print(j)
            else:
                print(j)

map = zeros((10, 10))
map[5][5] = 1

draw_map(map)