def boundary(v):
    i = 1
    bnd = 0
    if v == 1:
        print(1)
        return
    while(1):
        bnd += i*2
        if ((i-1)**2 < v <=bnd):
            print(i*2)
            return
        elif (bnd < v <= (i+1)**2):
            print(i*2+1)
            return 
        i+=1

t = int(input())
for i in range(t):
    x, y = map(int,input().split())
    boundary(y-x)
