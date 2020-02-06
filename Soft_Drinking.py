n,k,l,c,d,p,nl,np = map(int, input().split())

x1,x2,x3 = (k*l)//nl,c*d,p//np

print(min(x1,x3,x2)//n)
