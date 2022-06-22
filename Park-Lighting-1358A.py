for _ in range(int(input())):
    
    n,m = map(int, input().split())
    
    ans = (n*m) // 2
    
    print(ans if (n*m) % 2 == 0 else ans + 1)
