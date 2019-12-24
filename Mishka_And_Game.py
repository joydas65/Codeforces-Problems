m,c = 0,0

for _ in range(int(input())):
    
    mishka,chris = map(int, input().split())
    
    if mishka > chris:
        
        m += 1
        
    elif chris > mishka:
        
        c += 1
        
if c > m:
    
    print("Chris")
    
elif m > c:
    
    print("Mishka")
    
else:
    
    print("Friendship is magic!^^")
