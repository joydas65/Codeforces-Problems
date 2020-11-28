n = int(input())

arr = list(map(int, input().split()))

c = 0

for item in arr:
    
    if item == 5:
        
        c += 1
    
if n-c == 0:
    
    print(-1)
    
else:
    
    zeroes = n-c
    
    while c >= 1:
        
        if (c*5) % 9 == 0:
            
            print(("5"*c)+("0"*zeroes))
            
            break
        
        c -= 1
        
    if c == 0:
        
        print(0)
