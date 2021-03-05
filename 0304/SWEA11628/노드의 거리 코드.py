import sys
sys.stdin = open('input.txt')

def BFS(S, G):
    q = []
    visited = [0] * (V + 1)
    visited[S] = 1
    q.append(S)
    while q:
        target = q.pop(0)
        if target == G: break
        for i in AL[target]:
            if visited[i]: continue
            visited[i] = visited[target] + 1
            q.append(i)
    return visited

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V + 1)]
    for i in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)
    S, G = map(int, input().split())
    if BFS(S, G)[G] == 0:
        ans = 0
    else:
        ans = BFS(S, G)[G] - 1
    print('#%d %d' % (t, ans))