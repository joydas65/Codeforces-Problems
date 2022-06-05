for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    ind,num1,freq1,freq2,ans1,ans2 = 0,0,0,0,-1,-1
    
    while ind < n:
        
        if ind == 0:
            
            num1,freq1,ans1 = arr[0],1,0
            
        else:
            
            if arr[ind] != num1:
                
                freq2 += 1
                
                if freq2 == 1:
                    
                    ans2 = ind
                    
                else:
                    
                    print(ans2+1 if freq2 == 1 else ans1 + 1)
                    
                    break
                
            else:
                
                freq1 += 1
                
                if freq1 > 0 and freq2 > 0:
                    
                    print(ans2+1 if freq2 == 1 else ans1 + 1)
                    
                    break
                
        ind += 1
        
    if ind >= n:
        
        print(ans1+1 if freq1 == 1 else ans2+1)
