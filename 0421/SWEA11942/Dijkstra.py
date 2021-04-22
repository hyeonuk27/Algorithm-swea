import sys
sys.stdin = open('input.txt')


def Dijkstra(s):
    # 정점 s 방문 표시
    D = [100] * V
    visited = [0] * V
    D[s] = 0
    visited[s] = 1
    # 정점 s와 연결된 정점 e의 거리(d)를 D에 저장
    for e, d in AL[s]:
        D[e] = d
    # 최단 거리 찾기
    for _ in range(V-1):
        minD = 987654321
        for i in range(V):
            if not visited[i] and minD > D[i]:
                w, minD = i, D[i]
        visited[w] = 1
        for e, d in AL[w]:
            D[e] = min(D[e], D[w] + d)
    return D


for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    AL = [[] for _ in range(V)]
    for i in range(E):
        s, e, d = input().split()
        s, e, d = ord(s) - 97, ord(e) - 97, int(d)  # a = 0
        AL[s].append((e, d))
    print('#%d %s' % (t, ' '.join(map(str, Dijkstra(0)))))



