n = int(input())

i,j,k = 1,n*n,0

while k < n:

    for _ in range(n//2):
        
        print(i,end = " ")
        
        i += 1
        
    for _ in range(n//2):
        
        print(j,end = " ")
        
        j -= 1
        
    print()
    
    k += 1
