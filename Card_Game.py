for _ in range(int(input())):
    
    n,k1,k2 = map(int, input().split())
    
    kone = list(map(int, input().split()))
    
    ktwo = list(map(int, input().split()))
    
    maxkone,maxktwo = max(kone),max(ktwo)
    
    if maxktwo > maxkone:
        
        print("NO")
        
    else:
        
        print("YES")
