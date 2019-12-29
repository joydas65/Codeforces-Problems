for _ in range(int(input())):
    
    p = input()
    h = input()
    
    n1,n2 = len(p),len(h)
    
    if n1 > n2:
        
        print("NO")
        
    else:
        f = n1
        
        d = dict()
        
        for i in p:
            
            if i in d:
                
                d[i] += 1
                
            else:
                
                d[i] = 1
                
        i = 0
        
        while i+n1 <= n2:
            
            j,flag,f = i,0,n1
            
            while j < i+n1:
                
                if h[j] not in d:
                    
                    flag = 1
                    break
                else:
                    
                    if d[h[j]] > 0:
                        
                        d[h[j]] -= 1
                        f -= 1
                        
                    else:
                        flag = 1
                        break
                    
                j += 1
                
            if f == 0:
                
                break
                
            elif f > 0 and f < n1:
                
                d = dict()
                
                for k in p:
                    
                    if k in d:
                        
                        d[k] += 1
                        
                    else:
                        
                        d[k] = 1
                
            i += 1
                
        if f == 0:
            
            print("YES")
            
        elif i+n1 > n2:
            
            print("NO")
