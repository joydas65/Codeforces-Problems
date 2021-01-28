# Question Link

# http://codeforces.com/problemset/problem/433/B

n = int(input())

arr = list(map(int, input().split()))

ar = [arr[0]]

for i,j in enumerate(arr):
    
    if i >= 1:
        
        ar.append(ar[-1] + j)

arr = sorted(arr)

pre = [arr[0]]

for i,j in enumerate(arr):
    
    if i >= 1:
        
        pre.append(pre[-1] + j)

for _ in range(int(input())):
    
    type,l,r = map(int, input().split())
    
    if type == 2:
        
        print(pre[r-1] if l == 1 else pre[r-1] - pre[l-2])
        
    else:
        
        print(ar[r-1] if l == 1 else ar[r-1] - ar[l-2])
