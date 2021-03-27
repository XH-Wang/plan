# A* 算法介绍

## 学习资料
1. [中文博客：A星算法详解](https://blog.csdn.net/hitwhylz/article/details/23089415)

## 个人感悟
1. 启发式算法

## 启发函数h(n)设计原则
1. h(n) <= h*(n)
h(n) ：到目标节点的估计代价
h*(n): 到目标节点的实际代价

2. h(n) < c(n，n1) + h(n1)
h(n) ：到目标节点的估计代价
c(n，n1) : n到n1的代价

## 注意
1. 当保证h(n) <= h*(n)时，无需对close list进行检查