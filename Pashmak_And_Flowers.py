n = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)

beauty = arr[-1] - arr[0]

c1,c2 = 0,0

for i in arr:
    
    if i == arr[0]:
        
        c1 += 1
        
    elif i == arr[-1]:
        
        c2 += 1
        
if arr[0] == arr[-1]:
    
    print(beauty,(c1*(c1-1))//2)
    
else:
        
    print(beauty,c1*c2)
