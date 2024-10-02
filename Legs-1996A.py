for _ in range(int(input())):

    n = int(input())
    
    print(n//4 + (1 if n % 4 == 2 else 0))
