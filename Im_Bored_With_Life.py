a,b = map(int, input().split())

f,p = min(a,b),1

for i in range(1,f+1):
    
    p *= i
    
print(p)
