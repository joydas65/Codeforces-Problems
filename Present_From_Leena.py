n = int(input())

spaces = 2*n

for i in range(n+1):
    
    for _ in range(i,spaces):
        
        print('',end = " ")
    
    for j in range(i+1):
        
        if i == 0:
            
            print(0,end = "")
            
        else:
        
            print(j,end = " ")
        
    for j in range(i-1,-1,-1):
        
        if j == 0:
            
            print(j,end = "")
            
        else:
        
            print(j,end = " ")
        
    print()
    
    spaces -= 1
    
spaces = 2
    
for i in range(n,0,-1):
    
    for j in range(spaces):
        
        print('',end = " ")
        
    for j in range(i):
        
        if i == 1:
            
            print(0,end = "")
            
        else:
        
            print(j,end = " ")
        
    for j in range(i-2,-1,-1):
        
        if j == 0:
            
            print(j,end = "")
            
        else:
        
            print(j,end = " ")
        
    print()
    
    spaces += 2
