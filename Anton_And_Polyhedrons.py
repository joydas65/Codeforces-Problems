d = dict()

d["Icosahedron"] = 20
d["Cube"] = 6
d["Tetrahedron"] = 4
d["Dodecahedron"] = 12
d["Octahedron"] = 8

ans = 0

for _ in range(int(input())):
    
    ans += d[input()]
    
print(ans)
