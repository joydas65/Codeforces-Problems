n = int(input())

f,s = 0,str(n)

if s[0] != '1':
    
    print("NO")
    
else:
    
    for i,item in enumerate(s):
        
        if item not in ('1','4'):
            
            print("NO")
            
            f = 1
            
            break
        
        else:
            
            if item == '4':
                
                if i-1 >= 0 and s[i-1] == '4' and i-2 >= 0 and s[i-2] != '1':
                    
                    print("NO")
                    
                    f = 1
                    
                    break
                
    if f == 0:
        
        print("YES")
