for _ in range(int(input())):
    
    a,b,c = map(int, input().split())
    
    if c % 2 == 1:
        print("First" if a >= b else "Second")
    else:
        print("Second" if b >= a else "First")
