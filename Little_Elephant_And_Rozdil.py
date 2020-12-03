n = int(input())

arr = list(map(int, input().split()))

minValue,c,ans = min(arr),0,-1

for i,item in enumerate(arr):
    
    if item == minValue:
        
        c += 1
        
        ans = i
        
    if c == 2:
        
        print("Still Rozdil")
        
        break
    
if c == 1:
    
    print(ans+1)
