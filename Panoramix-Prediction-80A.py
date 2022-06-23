arr = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

n,m = map(int, input().split())

x = 0

for item in arr:
    
    if item == n:
        
        break
    
    x += 1
    
index_n = x
    
x = 0

for item in arr:
    
    if item == m:
        
        break
    
    x += 1
    
print("NO" if n == 47 else "YES" if x-index_n == 1 else "NO")
