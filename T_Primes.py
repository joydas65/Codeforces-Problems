import math
        
x = 10**6

prime = [True for i in range(x+1)]

prime[0],prime[1] = False,False

p = 2

while p*p <= x:
    
    if prime[p] == True:
        
        for i in range(p*p,x+1,p):
            
            prime[i] = False
            
    p += 1
        
n = int(input())

arr = list(map(int, input().split()))

for i in arr:

    root = math.sqrt(i)
    
    if int(root + 0.5) ** 2 == i and prime[int(root)] == True:
        
        print("YES")
        
    else:
        
        print("NO")
