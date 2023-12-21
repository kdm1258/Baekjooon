n = int(input())
relation = [[0 for columns in range(1,55)]for row in range(1,55)]
ans = [0]*55
def two_frd(v):
    cnt = 0
    c=[0]*(n+1)
    for i in range(1,n+1):
        if (relation[v][i] == 1 and c[v] != 1):
            cnt+=1
            c[i] = 1
            for j in range(1,n+1):
                if (c[j] != 1 and relation[i][j] == 1 and v!=j and relation[v][j] != relation[i][j]):
                    cnt+=1
                    c[j] = 1
    ans[v] = cnt

#배열 초기화
for i in range(1,n+1):
    str = list(input())
    for j in range(0,n):
        if (str[j]=='Y'):
            relation[i][j+1] = 1
for i in range(1,n+1):
    two_frd(i)
print((ans))
