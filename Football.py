s = input()

n,freq,flag = len(s),1,0

for i in range(1,n):
    
    if s[i] == s[i-1]:
        
        freq += 1
        
        if freq >= 7:
            
            print("YES")
            
            flag = 1
            
            break
        
    else:
        
        freq = 1
        
if flag == 0:
    
    print("NO")
