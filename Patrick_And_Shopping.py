a,b,c = map(int, input().split())

print(min((a+b+c),((2*a) + (2*b)),(b+c+(3*a)),(a+c+(3*b)),((2*b)+(2*c)),((2*a)+(2*c))))
