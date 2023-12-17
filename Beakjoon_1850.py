n, m = map(int,input().split())
if n>m:
    n,m = m,n
def gcd(a,b):
    if (a%b==0):
        return b
    else:
        return gcd(b, a%b)
    

k = gcd(m,n)
for i in range(k):
    print(1,end='')
