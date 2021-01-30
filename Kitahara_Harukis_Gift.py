# Question Link

# https://codeforces.com/problemset/problem/433/A

def findSubsetSum(ar, N, s):
    
    subset =[[False for i in range(s + 1)] for i in range(N + 1)]
    
    for i in range(N+1):
        
        subset[i][0] = True
        
    for i in range(1, s+1):
        
        subset[0][i] = False
        
    for i in range(1, N + 1):
        
        for j in range(1, s + 1):
            
            if j < ar[i-1]:
                
                subset[i][j] = subset[i-1][j]
                
            if j >= ar[i-1]:
                
                subset[i][j] = subset[i-1][j] or subset[i-1][j-ar[i-1]]
                
    return subset[N][s]

n = int(input())

arr = list(map(int, input().split()))

if findSubsetSum(arr, n, sum(arr)//2) == True:
    
    print("YES")
    
else:
    
    print("NO")
