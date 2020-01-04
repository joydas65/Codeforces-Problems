def findGCD(a,b):
    
    if a % b == 0:
        
        return b
        
    return findGCD(b, a%b)

a,b,n = map(int, input().split())

c,v = 0,a

while n > 0:
    
    x = findGCD(v,n)
        
    if n >= x:
        
        n -= x
        
    else:
        
        break
        
    c += 1
    
    if c % 2 == 1:
        
        v = b
        
    else:
        
        v = a
        
if c % 2 == 0:
    
    print(1)
    
else:
    
    print(0)
