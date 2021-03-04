import sys
sys.stdin = open('input.txt')

def BFS(sv):
    visited[sv] = True
    queue.append(sv)
    while queue:
        target = queue.pop(0)
        travel.append(target)
        for i in AL[target]:
            if visited[i]: continue
            visited[i] = True
            queue.append(i)
    return travel

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
    queue = []
    travel = []
    visited = [0] * (V + 1)
    ans = ' '.join(map(str, BFS(1)))
    print('#%d %s' % (t, ans))
