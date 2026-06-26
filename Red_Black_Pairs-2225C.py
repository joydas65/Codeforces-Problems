import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n = int(data.readline())
        top = data.readline().strip()
        bot = data.readline().strip()
        dp0 = 0
        dp1 = 1 if top[0] != bot[0] else 0
        for j in range(1, n):
            v = 1 if top[j] != bot[j] else 0
            ht = 1 if top[j - 1] != top[j] else 0
            hb = 1 if bot[j - 1] != bot[j] else 0
            cur = dp1 + v
            alt = dp0 + ht + hb
            if alt < cur:
                cur = alt
            dp0 = dp1
            dp1 = cur
        out.append(str(dp1))
    sys.stdout.write("\n".join(out) + "\n")

main()
