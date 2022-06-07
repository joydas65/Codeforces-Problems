arr = [0 for i in range(1000)]

i,x = 0,0

while x < 1000:
    
    if (i+1) % 3 != 0 and (i+1) % 10 != 3:
        
        arr[x] = i+1
        x += 1
    
    i += 1

for _ in range(int(input())):
    
    n = int(input())
    
    print(arr[n-1])
