'''
功能：轨迹类，保存规划输出结果
作者：Kirk
日期：2021.03.28
备注：
'''
import matplotlib.pyplot as plt

class trajectory:
    '''
    轨迹类
    '''
    def __init__(self):
        self.x = [] # 轨迹点x坐标
        self.y = [] # 轨迹点y坐标

    def plot(self):
        plt.plot(self.x, self.y, "-r",linewidth=3.0)

    def test_1(self):
        self.x = list(range(0,100))
        self.y[0:100] = list(range(0,100))

def main():
    path = trajectory()
    path.test_1()
    path.plot()

    plt.show()

if __name__ == "__main__":
    main()