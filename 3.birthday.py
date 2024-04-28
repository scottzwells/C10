import random

SIMULATION_TIMES = 100000  #模拟次数
people = 100  #人数

def generate_bir(people):
    '''随机生成生日'''
    birs = []
    for i in range(people):
        bir = random.randint(1, 365)  #不考虑闰年
        birs.append(bir)
    return birs

def check_bir(birs):
    '''检查是否有相同生日'''
    for bir in birs:
        if birs.count(bir) > 1:
            return True
    return False

# 100000次模拟
same_times = 0
for i in range(SIMULATION_TIMES):
    same_times += check_bir(generate_bir(people))   #记录符合次数
    if (i + 1) % 10000 == 0:    #实时报告进度
        print(f'目前已模拟{i + 1}组数据, 符合 {same_times}组, 实时概率为 {same_times * 100 / (i + 1)}%')