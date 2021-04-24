import sys
sys.stdin = open('input.txt')

operator = [lambda x: x + 1, lambda x: x - 1, lambda x: x * 2, lambda x: x - 10]

def cal(sv):
    v = [0] * 1000001
    q = [sv]
    rp = 0
    v[sv] = 1

    while True:
        x = q[rp]
        rp += 1
        if x == M:
            return v[x] - 1
        for o in operator:
            nx = o(x)
            if 0 < nx <= 1000000 and not v[nx]:
                v[nx] = v[x] + 1
                q.append(nx)

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    print('#%d %d' % (t, cal(N)))