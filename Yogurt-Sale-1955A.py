for _ in range(int(input())):
    
    n,a,b = map(int, input().split())
    
    ans = n//2 * min(2*a,b)
    
    print(ans + a if n % 2 == 1 else ans)
