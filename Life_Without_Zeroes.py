a = int(input())

b = int(input())

c = a+b

a_without_zero = ""

for item in str(a):
    
    if item != '0':
    
        a_without_zero = a_without_zero + item
        
b_without_zero = ""

for item in str(b):
    
    if item != '0':
        
        b_without_zero = b_without_zero + item
        
c_without_zero = ""

for item in str(c):
    
    if item != '0':
        
        c_without_zero = c_without_zero + item
        
#print(a_without_zero,b_without_zero,c_without_zero)
        
if int(a_without_zero) + int(b_without_zero) == int(c_without_zero):
    
    print("YES")
    
else:
    
    print("NO")
