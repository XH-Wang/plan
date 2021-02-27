from matplotlib import *
import matplotlib.pyplot as plt

from numpy import *

def draw_map(map):
    '''
    绘制地图
    ''' 
    for i in map:
        for j in i:
            if 0 != j:  
                print(j)
            else:
                print(j)
    
    plt.grid(True)  #开启栅格
    plt.scatter(1, 1, s=500, c='black', marker='s')
    plt.title("grid map simulation ")
    plt.show()

map = zeros((10, 10))
map[5][5] = 1

draw_map(map)