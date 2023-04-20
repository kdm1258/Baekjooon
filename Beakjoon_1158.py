n, k = map(int, input().split())
queue = list(range(1,n+1))
Yos = []
tmp = 0 
buf = k-1 #변수에 k-1값을 저장하는데 이때 k-1인 이유는 요세푸스 수열의 인자가 추가될 때마다 queue의 인자수가 줄어들기에 k-1만큼의 인덱스 이동이 필요하다
i = 1
for j in range(1,n+1):
    tmp += buf
    while ((n-j) < tmp ):
        tmp = (tmp-(n-j)-1)
    Yos.append(queue[tmp])
    queue.pop(tmp)

print(str(Yos).replace('[', '<').replace(']', '>'))



#처음에는 반복문의 j를 이용해 tmp = tmp*j의 형식으로 문제풀이를 하려고 하였으나 이럴 경우 tmp의 값이 변해 
