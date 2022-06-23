for _ in range(int(input())):
    
    s = input()
    
    if ord(s[0]) + ord(s[1]) + ord(s[2]) == ord(s[3]) + ord(s[4]) + ord(s[5]):
        print("YES")
    else:
        print("NO")
