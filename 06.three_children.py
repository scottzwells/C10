age={}
for i in range(1,4):
    for j in range(i,7):
        k=36/(i*j)
        if k%1==0 and k>=j:
            k=int(k)
            age.setdefault((i,j,k),i+j+k)

rep = 0
for value in list(age.values()):
    if list(age.values()).count(value)>=2:
        rep = value

store=[]
count=0
for a in range(0,len(age)):
    if list(age.values())[a]==rep:
        store.append(list(age.keys())[a])
        count+=1
for x in range(count):
    count=0
    if store[x][2]>store[x][1]:
        print(store[x])
        count+=1

if count==0:
    print("不存在这样的情况")

