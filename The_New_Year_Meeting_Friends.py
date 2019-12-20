a,b,c = map(int, input().split())

m1,m2,m3 = min(a,b,c),0,max(a,b,c)

if (m1 == a and m3 == b) or (m1 == b and m2 == a):
    
    m2 = c
    
elif (m1 == a and m3 == c) or (m1 == c and m3 == a):
    
    m2 = b
    
elif (m1 == b and m3 == c) or (m1 == c and m3 == b):
    
    m2 = a
    
print((m2-m1)+(m3-m2))
