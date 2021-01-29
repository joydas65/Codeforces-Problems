# https://codeforces.com/problemset/problem/1399/B

# Question Link

for _ in range(int(input())):
    
    n = int(input())
    
    candies = list(map(int, input().split()))
    
    oranges = list(map(int, input().split()))
    
    minCandy,minOrange = min(candies),min(oranges)
    
    ans = 0
    
    for i,j in enumerate(candies):
        
        if j == minCandy and oranges[i] != minOrange:
            
            ans += (oranges[i] - minOrange)
            
        elif oranges[i] == minOrange and j != minCandy:
            
            ans += (j - minCandy)
            
        elif j > minCandy and oranges[i] > minOrange:
            
            v = min(j-minCandy,oranges[i]-minOrange)
            
            ans += v
            
            ans += (max(j-minCandy,oranges[i]-minOrange) - v)
            
    print(ans)
