import sys
sys.stdin = open('input.txt')

# Dfs 함수
# stack 초기값으로 chk_s를 넣고, visited를 반환
# visited[chk_e]에 1이 있으면 경로 있다!
def DFS(V, AL, sv):
    visited = [0] * (V + 1)
    stack = [sv]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            for i in AL[node]:
                if not visited[i]:
                    stack.append(i)
    return visited

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split()) # 노드와 간선
    edges = [tuple(map(int, input().split())) for _ in range(E)] # 경로
    chk_s, chk_e = map(int, input().split()) # 찾고자 하는 경로

    # AL 만들기
    AL = [[] for _ in range(V + 1)]
    for s, e in edges:
        AL[s].append(e)

    ans = 1 if DFS(V, AL, chk_s)[chk_e] else 0
    print('#%d %d' % (t, ans))