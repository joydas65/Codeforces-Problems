for _ in range(int(input())):
    
    n = int(input())
    
    word = input()
    
    if n > 5 or n < 5:
        print("NO")
    else:
        print("YES" if 'T' in word and 'i' in word and 'm' in word and 'u' in word and 'r' in word else "NO")
