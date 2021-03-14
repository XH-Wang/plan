"""
A* algorithm
Author: Kirk

Reference
1. https://blog.csdn.net/hitwhylz/article/details/23089415
"""
# from matplotlib import *
# #import matplotlib.pyplot as plt
# from pylab import *
# import copy

# from numpy import *

# restrict map's scope
top_vertex = [100, 100]
bottom_vertex = [0, 0]

def random_coordinate_2d():
    '''
    generate 2d random coordinate
    '''
    coordinate = [0, 0]
    return coordinate

def main ():
    coordinate = random_coordinate_2d()
    print(coordinate)


if __name__ == "__main__":
    main()

# class map:
#     def __init__(self):
        

# def draw_map(map):
#     '''
#     绘制地图
#     ''' 
#     for i in map:
#         for j in i:
#             if 0 != j:  
#                 print(j)
#             else:
#                 print(j)
    
#     plt.grid(True)  #开启栅格
#     plt.xlim(-1, 20)  # 设置x轴范围
#     plt.ylim(-1, 20)  # 设置y轴范围
#     my_x_ticks = arange(0, 20, 1)
#     my_y_ticks = arange(0, 20, 1)
#     plt.xticks(my_x_ticks)
#     plt.yticks(my_y_ticks)  
#     plt.scatter(1, 1, s=500, c='black', marker='s', cmap=None, norm=None, vmin=10, vmax=100, alpha=None, linewidths=1)
#     plt.title("grid map simulation ")
#     plt.show()


# map = zeros((10, 10))
# map[5][5] = 1

# map_grid = numpy.full((20, 20), int(10), dtype=numpy.int8)
# map_grid[3, 3:8] = 0
# map_grid[3:10, 7] = 0
# map_grid[10, 3:8] = 0
# map_grid[17, 13:17] = 0
# map_grid[10:17, 13] = 0
# map_grid[10, 13:17] = 0
# map_grid[5, 2] = 7
# map_grid[15, 15] = 5

# plt.imshow(map_grid, cmap=plt.cm.hot, interpolation='nearest', vmin=0, vmax=10)
# # xlim(-1, 20)  # 设置x轴范围
# # ylim(-1, 20)  # 设置y轴范围
# # my_x_ticks = numpy.arange(0, 20, 1)
# # my_y_ticks = numpy.arange(0, 20, 1)
# # plt.xticks(my_x_ticks)
# # plt.yticks(my_y_ticks)
# # plt.grid(True)
# plt.show()
# #draw_map(map)