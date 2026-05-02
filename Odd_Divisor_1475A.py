import sys
input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    out.append("NO" if (n & (n - 1)) == 0 else "YES")
print("\n".join(out))
