import sys

def push(k):
    my_list.append(k)
  

def pop():
    if len(my_list) != 0:
        result.append(my_list[-1])
        my_list.pop()

    else:
        result.append(-1)
  

def empty():
    if len(my_list) == 0:
        result.append(1)
    else:
        result.append(0)
  

def top():
    if len(my_list) == 0:
        result.append(-1)
    else:
        result.append(my_list[-1])
   
    
def size():
    result.append(len(my_list))
   

my_list = []
result = []

n = int(input())

for i in range(n):
    word = sys.stdin.readline().split()
    a = word[0]
        
    if a == "pop":
        pop()
        
    elif a == "size":
        size()

    elif a == "empty":
        empty()

    elif a == "top":
        top()
        
    else:
        b = word[1]
        push(int(b))
        
for j in range(len(result)):
    print(result[j])
