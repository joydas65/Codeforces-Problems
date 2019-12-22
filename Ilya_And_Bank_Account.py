n = int(input())

h = str(n)

x = len(h)

a = int(h[:x-1])

b = int(h[:x-2] + str(h[-1]))

if a >= n and a >= b:
    
    print(a)
    
elif b >= n and b >= a:
    
    print(b)
    
else:
    
    print(n)
