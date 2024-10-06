for _ in range(int(input())):
    
    n = int(input())
    
    if n == 1:
        print(0)
    else:
        count2,count3 = 0,0
        
        while n%2 == 0:
            count2 += 1
            n//=2
            
        while n%3 == 0:
            count3 += 1
            n//=3
            
        if n != 1 or count2 > count3:
            print(-1)
        else:
            print(2*count3 - count2)
