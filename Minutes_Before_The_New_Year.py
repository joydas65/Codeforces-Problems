for _ in range(int(input())):

    hours,minutes = map(int, input().split())
    
    print((23 - hours)*60 + (60 - minutes))
