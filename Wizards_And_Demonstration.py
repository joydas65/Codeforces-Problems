import math

n,x,y = map(int, input().split())

v = int(math.ceil((y * n)/100))

if v > x:
    
    print(v - x)
    
else:
    
    print(0)
