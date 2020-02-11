n = int(input())

arr = list(map(int, input().split()))

x = arr.copy()

x,i,f,start,end,v = sorted(x),0,0,0,0,0

while i < n:
    
    if f == 0 and arr[i] != x[i]:
        
        f = 1
        start,v = i,x[i]
        
    elif f == 1 and arr[i] == v:
        end = i
        break
    
    i += 1

if start == 0:
    
    if end == n-1:
        
        if arr[::-1] == x:
            print("yes")
            print(start+1,n)
        else:
            print("no")
        
    else:
        arr = arr[:end+1][::-1] + arr[end+1:]
        if arr == x:
            print("yes")
            print(start+1,end+1)
        else:
            print("no")
            
elif end == n-1:
    
    arr = arr[:start] + arr[start:][::-1]
    if arr == x:
        print("yes")
        print(start+1,n)
    else:
        print("no")
        
else:
    
    arr = arr[:start] + arr[start:end+1][::-1] + arr[end+1:]
    if arr == x:
        
        print("yes")
        print(start+1,end+1)
    else:
        print("no")
        
#print(start,end)
