n,m,r = map(int, input().split())

prev = r

s = list(map(int, input().split()))

b = list(map(int, input().split()))

s_min = min(s)

shares = r//s_min

r -= (shares*s_min)

b_max = max(b)

r += (shares*b_max)

print(max(r,prev))
