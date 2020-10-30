#Link to the question
#https://codeforces.com/problemset/problem/1399/A

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    if n == 1:
        
        print("YES")
        
    else:
        
        arr = sorted(arr)
        
        i,f = 0,True
        
        while i < (n-1):
            
            if arr[i+1] - arr[i] > 1:
                
                f = False
                
                break
            
            i += 1
            
        print("YES" if f == True else "NO")
