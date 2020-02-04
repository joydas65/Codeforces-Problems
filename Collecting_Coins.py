for _ in range(int(input())):
    
    a,b,c,n = map(int, input().split())
    
    if (a+b+c+n)%3 == 0:
        x = (a+b+c+n)//3
        if x >= a and x >= b and x >= c:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
