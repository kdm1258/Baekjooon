n, m, v = map(int,input().split())
arr = [[0 for col in range(1001)]for row in range(1001)]
d =[0]*1001
b =[0]*1001

def DFS(v):
    if (d[v] == 0):
        print(v, end = ' ')
    d[v] = 1
    for i in range(1,n+1):
        if (d[i]!=1 and arr[v][i]):
            DFS(i)
def BFS(v):
    queue = [v]
    b[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end = ' ')
        for i in range(1,n+1):
            if (b[i] != 1 and arr[v][i]):
                queue.append(i)
                b[i] = 1




#array 입력받기
for i in range(1,m+1):
    tmp1, tmp2 = map(int,input().split())
    arr[tmp1][tmp2] = 1
    arr[tmp2][tmp1] = 1

DFS(v)
print()
BFS(v)
