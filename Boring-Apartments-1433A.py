for _ in range(int(input())):
    
    n = int(input())
    
    digit,ans,num = 1,1,1
    
    while num != n and digit < 10:
        
        num = (num*10) + digit
        
        ans += len(str(num))
        
        if num == n:
        	break
        
        if len(str(num)) == 4:
            
            digit += 1
            
            num = digit
            
            if digit < 10:
            	ans += 1
            
    print(ans)
