n,t = map(int, input().split())

arr = list(map(int, input().split()))

i = 0

while i != (t-1) and i < n-1:
    
    #print(i)
    
    i = (i+1) + arr[i] - 1
    
if i >= n-1 and i != (t - 1):
    
    print("NO")
    
else:
    
    print("YES")
