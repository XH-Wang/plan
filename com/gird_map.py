'''
功能：产生栅格地图
作者：Kirk
日期：2021.03.27
备注：
'''
import numpy as np
import matplotlib.pyplot as plt

class gird_map:
    '''
    栅格地图类
    '''
    def __init__(self, x_length = 100, y_length = 100, start = [0, 50], end = [99, 50]):
        self.x_length = x_length
        self.y_length = y_length

        self.data = np.zeros([self.x_length, self.y_length])

        self.start = start # 规划起点
        self.end = end # 规划终点
    
    def plot_map(self):
        '''
        绘制栅格地图地图信息
        '''
        # 绘制地图
        x = []
        y = []

        for i in range(0, self.x_length):
            for j in range(0, self.y_length):
                if 0 != self.data[i,j]:
                    x.append(i)
                    y.append(j)

        plt.plot(x, y, ".k")

    def plot(self):
        '''
        绘制栅格地图、起点、终点
        '''
        # 绘制地图
        self.plot_map()

        plt.plot(self.start[0], self.start[1], "or")
        plt.plot(self.end[0], self.end[1], "*r")

    def test_1(self):
        '''
        障碍物地图测试样例1
        '''
        self.data[int(self.x_length * 0.3), 0 : int(self.y_length * 0.8)] = 1

    def test_2(self):
        '''
        障碍物地图测试样例2
        '''
        self.data[int(self.x_length * 0.3), 0 : int(self.y_length * 0.8)] = 1
        self.data[int(self.x_length * 0.6), int(self.y_length * 0.2) : self.y_length] = 1


def main():
    print("地图类测试")
    map = gird_map()
    map.test_1()
    map.plot()

    plt.show()

    print("地图", map.data)
    
if __name__ == "__main__":
    main()
