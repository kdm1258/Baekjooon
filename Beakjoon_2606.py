n = int(input())
m = int(input())
arr = [[0 for col in range(101)]for row in range(101)]
check =[0]*101
global cnt
cnt = 0

def DFS(v):
    global cnt
    check[v] = 1
    for i in range(1,n+1):
        if (check[i]!=1 and arr[v][i]):
            cnt+=1
            DFS(i)

def BFS(v):
    queue = [v]
    check[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1,n+1):
            if (check[i] != 1 and arr[v][i]):
                queue.append(i)
                b[i] = 1

#배열 초기화            
for i in range(m):
    tmp1, tmp2 = map(int,input().split())
    arr[tmp1][tmp2] = 1
    arr[tmp2][tmp1] = 1

DFS(1)
print(cnt)
