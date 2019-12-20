n,k = map(int, input().split())

lb,ub = 1,n

while lb <= ub:
    
    mid = (lb + ub)//2
    
    s = (mid * (mid + 1))//2
    
    s = s*5
    
    if s + k <= 240:
        
        lb = mid + 1
        
    else:
        
        ub = mid - 1
        
print(ub)
