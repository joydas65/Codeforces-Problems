for _ in range(int(input())):
    
    s = input()
    
    n = len(s)
    
    if n > 3 or n < 3:
        print("NO")
    else:
        c1,c2,c3 = ord(s[0]),ord(s[1]),ord(s[2])
        if (c1 == 121 or c1 == 89) and (c2 == 101 or c2 == 69) and (c3 == 115 or c3 == 83):
            print("YES")
        else:
            print("NO")
