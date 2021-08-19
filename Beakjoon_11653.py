NUM = int(input())

i = 2

if NUM == 1:
    print()
else:
    
    while NUM != 1:
        if NUM % i == 0:
            print(i)
            NUM /= i
            continue
        else:
            i += 1
            
