def jump(steps):
    if steps in (1,2):
        return steps
    else:
        m,n=1,2
        for i in range(steps-2):
            m,n=n,m+n
        return  n

print(jump(100))
