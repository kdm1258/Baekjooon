n ,k = map(int, input().split())
d = [[0 for columns in range(k+1)]for row in range(n+1)]
w = [0]*(n+1)
v = [0]*(n+1)

for i in range(1,n+1):
    w[i], v[i] = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,k+1):
        if (j-w[i]>=0):  #가방의 현재 공간 j -물건의 무게가 0보다 크다면 i번째물건 넣든지 말든지 선택
            d[i][j] = max(d[i-1][j], d[i-1][j-w[i]]+v[i])
        else:          #가방의 공간이 안되면 그냥 안넣기
            d[i][j] = d[i-1][j]
print(d[n][k])
