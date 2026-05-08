import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
out = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    odd_count = sum(1 for v in Counter(s).values() if v % 2 == 1)
    out.append("YES" if odd_count <= k + 1 else "NO")
print('\n'.join(out))
