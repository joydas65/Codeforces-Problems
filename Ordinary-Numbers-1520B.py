for _ in range(int(input())):
    
    n = int(input())
        
    if n < 10:
        
        print(n)
        
    else:
        
        answer = 9
        
        num = 10
        
        i,flag = 1,0
        
        while flag == 0:
            
            i,flag = 1,0
        
            while i <= 9:
                
                if ((i*num) + i) <= n:
                    
                    answer += 1
                    
                else:
                    
                    flag = 1
                    
                    break
                    
                i += 1
                
            num = (num * 10) + 10
            
        print(answer)
