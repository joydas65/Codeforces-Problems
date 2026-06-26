import sys

def main():
    data = sys.stdin.buffer
    t = int(data.readline())
    out = []
    for _ in range(t):
        n, k = map(int, data.readline().split())
        a = sorted(map(int, data.readline().split()))
        ans = "NO"
        i = 0
        while i < n:
            j = i
            distinct = 1
            while j + 1 < n and a[j + 1] - a[j] <= k:
                if a[j + 1] != a[j]:
                    distinct += 1
                j += 1
            count = j - i + 1
            if distinct >= 2 or count % 2 == 0:
                ans = "YES"
                break
            i = j + 1
        out.append(ans)
    sys.stdout.write("\n".join(out) + "\n")

main()
