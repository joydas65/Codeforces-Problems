n = int(input())

arr = list(map(int, input().split()))

arr,f = sorted(arr),0

for i,j in enumerate(arr):
    
    if i+1 != j:
        
        print(i+1)
        
        f = 1
        
        break
    
if f == 0:
    
    print(n+1)
