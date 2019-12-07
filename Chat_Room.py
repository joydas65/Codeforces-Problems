s = input()

j,n,freq = 0,len(s),0

for i in "hello":
    
    while j < n:
        
        if s[j] == i:
            
            freq += 1
            
            j += 1
            
            break
        
        j += 1
        
    if j == n:
        
        break
    
if freq == 5:
    
    print("YES")
    
else:
    
    print("NO")
