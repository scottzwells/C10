def move(x,y,count):
    """该函数用于移动圆盘"""
    print(f"{x}-->{y}")
    return count+1

def hanoi(n,a,b,c,count):
    """将问题逐步分解为n-1级汉诺塔问题"""
    if n==1:  count= move(a,c,count)
    else:
        count = hanoi(n-1,a,c,b,count)
        count = move(a,c,count)
        count = hanoi(n-1,b,a,c,count)
    return count


while True:
    n = input("输入汉诺塔层数：")
    if str.isdigit(n) :                    #判断输入是否为数字
        if int(n)>0:                       #判断层数大于0
           n = int(n)
           count = hanoi(n,'A','B','C',0)         #用A，B，C来分别表示左、中、右柱
                                               #初始时记count为0次
           print(f"总共进行了{count}次移动。")
        else:break
    else: break
