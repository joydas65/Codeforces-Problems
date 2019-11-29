n,m,a = map(int, input().split())

tiles_along_length,tiles_along_breadth = 0,0

if n % a == 0:
    
    tiles_along_length = n//a
    
else:
    
    tiles_along_length = (n//a) + 1
    
if m % a == 0:
    
    tiles_along_breadth = m//a
    
else:
    
    tiles_along_breadth = (m//a) + 1
    
print(tiles_along_breadth * tiles_along_length)
