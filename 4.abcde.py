def trans(num):
    n=0
    for i in range(5):
        n+=num[i]*(10**(4-i))
    return n

def multi(num,times=4):
    """将数组表示的数乘上4倍"""
    num4=num[:]
    flag=0
    for i in range(4,-1,-1):
        num4[i]*=times
        num4[i]+=flag
        flag=int(num4[i]/10)
        num4[i]=num4[i]%10
    return num4

def check(num):
   num4=multi(num)
   verify=0
   for i in (0,1,3,4):
       if num[i]==num4[4-i]: verify+=1
   if verify==4: print(trans(num))

num=[0,0,0,0,0]
for a in range(1,3):
    num[0]=a
    for b in range (0,15-5*a):
        if b in num[:1]:continue
        num[1]=b
        for c in range(0,10):
            if c in num[:2]: continue
            num[2]=c
            for d in range(0, 10):
                if d in num[:3]: continue
                num[3] = d
                for e in range(0, 10):
                    if e in num[:4]: continue
                    num[4] = e
                    check(num)