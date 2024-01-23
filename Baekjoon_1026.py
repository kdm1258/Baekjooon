n = int(input())
arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))

#A배열을 정렬, B배열을 내림차순 정렬한 뒤 곱해준 값을 더한다
arr_A.sort()
arr_B.sort(reverse=True)

sol = 0
for i in range(n):
    sol += arr_A[i]*arr_B[i]

print(sol)
