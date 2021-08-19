n = int(input())
a = list(map(int, input().split()))
cnt = 0
b = 0
    
for i in range(0,n):
    cnt = 0
    for j in range(1,a[i] + 1):
        if a[i] % j == 0:
                cnt+=1
                        
    if cnt == 2:
        b += 1
print(b)
