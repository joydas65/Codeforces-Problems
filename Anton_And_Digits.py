k2,k3,k5,k6 = map(int, input().split())

d,ans = dict(),0
d[2] = k2
d[3] = k3
d[5] = k5
d[6] = k6
v = min(d[2],d[5],d[6])
ans = 256*v
d[2] -= v

if d[2] >= 1:
    ans += 32*min(d[2],d[3])

print(ans)
