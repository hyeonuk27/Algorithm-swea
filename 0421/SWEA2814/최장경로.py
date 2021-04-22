import sys
sys.stdin = open('input.txt')

def DFS(sv, cnt):
    global ans
    ans = max(cnt, ans)
    for n in AL[sv]:
        if visited[n]: continue
        visited[n] = 1
        DFS(n, cnt+1)
        visited[n] = 0


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        AL[s].append(e)
        AL[e].append(s)
    ans = 0
    for sv in range(1, V+1):
        visited = [0] * (V+1)
        visited[sv] = 1
        DFS(sv, 1)
        visited[sv] = 0
    print('#%d %d' % (t, ans))