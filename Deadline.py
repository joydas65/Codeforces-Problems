import math

for _ in range(int(input())):
    
    n,d = map(int, input().split())
    
    if d <= n:
        
        print("YES")
        
    else:
        
        lb,ub,flag = 0,n,0
        
        while lb < ub:
            
            mid = (lb + ub)//2
            
            v = mid + int(math.ceil(d/(mid+1)))
            
            if v <= n:
                flag = 1
                break
            else:
                ub = mid
                
        if lb == ub:
            v = lb + int(math.ceil(d/(lb+1)))
            
            if v <= n:
                flag = 1
                
        if flag == 1:
            print("YES")
            
        else:
            print("NO")
