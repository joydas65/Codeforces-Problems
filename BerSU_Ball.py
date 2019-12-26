n = int(input())

boys = list(map(int, input().split()))

m = int(input())

girls = list(map(int, input().split()))

boys = sorted(boys)

girls = sorted(girls)

i,j,ans = 0,0,0

while i < n and j < m:
    
    if abs(boys[i]-girls[j]) <= 1:
        
        ans += 1
        
        i += 1
        
        j += 1
        
    else:
        
        if boys[i] < girls[j]:
            
            i += 1
            
        elif girls[j] < boys[i]:
            
            j += 1
            
print(ans)
