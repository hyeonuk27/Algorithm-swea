import sys
sys.stdin = open('input.txt')

operator = [(lambda x: x + 1), (lambda x: x - 1), (lambda x: x * 2), (lambda x: x - 10)]

def cal():
    q = [N]
    visited = [0] * 1000001
    visited[N] = 1
    rp = 0
    while q:
        x = q.pop(rp)
        rp += 1
        if x == M:
            return visited[x] - 1
        for o in operator:
            nx = o(x)
            if nx <= 1000000 and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    print('#%d %d' %(t, cal()))
