pq = []
for _ in range(int(input())):
    
    quantity,price = map(int, input().split())
    pq.append((quantity,price))
ans,v,w = 0,pq[0][1],pq[0][0]

for i,j in enumerate(pq):
    
    if i == 0:
        continue
    
    if v <= j[1]:
        w += j[0]
    else:
        ans += (w * v)
        w = j[0]
        v = j[1]
print(ans + (w*v))
