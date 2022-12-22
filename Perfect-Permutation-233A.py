n = int(input())

if n % 2 == 1:
    print(-1)
else:
    i = 1
    
    while i <= n//2:
        
        print(2*i,end = " ")
        print((2*i)-1,end = " ")
        
        i += 1
