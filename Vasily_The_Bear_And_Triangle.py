x,y = map(int, input().split())

if x > 0 and y > 0:
    
    print(0,x+y,x+y,0)
    
elif x < 0 and y > 0:
    
    print(x-y,0,0,abs(x-y))
    
elif x < 0 and y < 0:
    
    print(x+y,0,0,x+y)
    
else:
    
    print(0,-1*(x-y),x-y,0)
