import numpy as np
a = input("Enter numbers in a separately: ").split()
a = [int(x) for x in a]
b = input("Enter numbers in b separately: ").split()
b = [int(x) for x in b]

c=a+b
N=len(c)

negative=0 if min(c)>=0 else min(c)
negative=-negative+100 if max(c)<100 else max(c)
c=[i+negative for i in c]   #整体平移
M=sum(c)//2+1                        #当前容量
Q=N//2+1                                  #项数数/2
N=N+1                                     #元素项数
bag=np.zeros((Q,M,N),dtype=int )

for i in range(1,N):
    for j in range(1,M):
        for k in range (1,Q):
            if(j>=c[i-1]):
                bag[k,j,i]=max(bag[k][j][i-1],bag[k-1][j-c[i-1]][i-1]+c[i-1])
            else:
                bag[k][j][i]=bag[k][j][i-1]

deal,i,j,k=0,N-1,M-1,Q-1
while True:
    if(bag[k,j,i]!=bag[k,j,i-1]):
        a[deal]=c[i-1]
        deal+=1
        j-=c[i-1]
        i-=1
        k-=1
    else:
        i-=1
    if j==0 or i==0 or k==0:
        break

N=N-1

for i in range(N//2):
    for j in range(N):
        if(a[i]==c[j]):
            c[j]=0
            break
i=0
for j in range(N):
    if(c[j]!=0):
        b[i]=c[j]
        i+=1

a=[i-negative for i in a]
b=[i-negative for i in b]
print(f"已完成交换，a={a}，b={b}，和之差为{abs(sum(a)-sum(b))}")

