import sys
sys.stdin = open('input.txt')

# DFS 함수 구현해서, visited[99]를 리턴 받기
def DFS(V, AL, sv):
    visited = [0] * (V + 1)
    stack = [sv]
    while stack:
        node = stack.pop(-1)
        if not visited[node]:
            visited[node] = 1
            for i in AL[node]:
                if not visited[i]:
                    stack.append(i)
    return visited[99]

for t in range(1, 11):
    tc, n = map(int, input().split())
    nums = list(map(int, input().split()))
    V = 99
    # 두 개씩 튜플로 묶어주기
    edges = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
    # 인접 리스트 만들기
    AL = [[] for _ in range(V + 1)]
    for s, e in edges:
        AL[s].append(e)

    ans = 0 if DFS(V, AL, 1) == 0 else 1

    print('#%d %d' % (t, ans))