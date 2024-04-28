def check(hats,else1,else2):
    """该函数用于判断某人是否能通过其余两人帽子颜色来判断自己帽子颜色，
        同时排除掉A与B能直接判断出的情况"""
    temp = []
    n = len(hats)
    for x in range(n):
        flag = 0
        hat1 = hats[x]
        for y in range(n):
            if y == x: continue
            hat2 = hats[y]
            if (hat1[else1] == hat2[else1] and hat1[else2] == hat2[else2]):
                flag = 1
        if flag == 1:
            temp.append(hat1)
    return temp


hats=[]                           #创建存放所有可能性的列表
for i in range(2):
    for j in range(2):
        for k in range(2):
            if not i and not j and not k ==1:
                continue
            hats.append((i,j,k))   #用1表示红帽子，0表示白帽子
print(f"初始情况如下：\n{hats}。")

hats=check(hats,1,2)          #检查A是否能判断出自己帽子颜色
print(f"A说完后可能性还剩下:\n{hats}")

hats=check(hats,0,2)          #检查B是否能判断出自己帽子颜色
print(f"B说完后可能性只有:\n{hats}")

print("剩余情况中C的帽子颜色只可能是红色，故C可判断出所有人的帽子颜色")