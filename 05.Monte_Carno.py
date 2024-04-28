#采用蒙特卡洛法计算圆周率
from random import random

points = 10**7  #总样本数
count = 0
for i in range(points):
    x,y = random(),random() #随机生成坐标
    dis = (x**2+y**2)**0.5
    if dis<=1.0 :
        count+=1
    if i%10**6 == 0 and i!=0 :
        print(f"已处理{i}组数据({i//10**5}%)")
pi=(count/points)*4
print(f"样本容量{points}，以蒙特卡洛法计算的圆周率为：{pi}。")
