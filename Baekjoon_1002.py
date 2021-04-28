cnt = int(input())
a = []
for j in range(cnt):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    d = (((x1-x2)**2)+((y1-y2)**2))**(1/2)
    if ( d == 0 and r1 == r2):
        a.append(-1)
    elif ( d == 0 and r1 != r2):
        a.append(0)
    elif (d == r1 + r2 or abs(r1-r2) == d):
        a.append(1)
    elif (abs(r1 - r2) < d < r1 + r2 ):
        a.append(2)
    elif (abs(r1 - r2) > d or d> r1 + r2):
        a.append(0)
   
for i in a:
    print(i)
