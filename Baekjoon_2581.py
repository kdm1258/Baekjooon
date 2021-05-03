N = int(input())
M = int(input())
a = []

for i in range(N, M+1):
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
            
    if cnt == 2:
        a.append(i)
print(a)

if len(a) == 0 :
    print(-1)
else:
    print(sum(a))
    print(a[0])
