v, e = 7, 8
edges = [(1, 2), (1, 3),(2 , 4), (2, 5), (4, 6), (5, 6), (6, 7), (3, 7)]

# 인접행(Matrix) = V*V
AM = [[0] * (v+1) for _ in range(v+1)]

for s, e in edges:
    AM[s][e] = 1
    AM[e][s] = 1

# 인접 리스트(list) = V
AL = [[] for _ in range(v+1)]
for s, e in edges:
    AL[s].append(e)
    AL[e].append(s)


# DFS 함수 만들기
# AM 사용해서
def DFS(V, AM, sv):
    # 방문 여부 체크할 공간 만들기
    visited = [0] * (V+1)
    ##### 방문 순서를 기록하고 싶으면 추가 ######
    travel = []
    # 스택에 시작 정점을 push
    stack = [sv]
    # 스택에 내용이 있는 동안만 반복
    # while len(stack):
    while stack:
        # 스택에서 pop해서 node에 저장
        node = stack.pop(-1)
        # 방문했는지 확인해서 방문을 안했을 때 true 표시
        if not visited[node]:
            # 방문 표시를 한다.
            visited[node] = 1
            ##### 방문 순서 체크를 하기 위해서는 여기에 들어와야 함 #####
            travel.append(node)
            # 그 노드에 연결되어 있으면서 방문하지 않은 노드를 탐색해서 스택에 push
            for c in range(1, v+1):
                if AM[node][c] == 1 and visited[c] == 0:
                    stack.append(c)
    # DFS의 while을 끝낸 시점
    print(stack)
    print(visited)
    print(tavel)


# DFS 함수 만들기
# AL 사용해서
def DFS(V, AL, sv):
    # 방문 여부 체크할 공간 만들기
    visited = [0] * (V+1)
    ##### 방문 순서를 기록하고 싶으면 추가 ######
    travel = []
    # 스택에 시작 정점을 push
    stack = [sv]
    # 스택에 내용이 있는 동안만 반복
    # while len(stack):
    while stack:
        # 스택에서 pop해서 node에 저장
        node = stack.pop(-1)
        # 방문했는지 확인해서 방문을 안했을 때 true 표시
        if not visited[node]:
            # 방문 표시를 한다.
            visited[node] = 1
            ##### 방문 순서 체크를 하기 위해서는 여기에 들어와야 함 #####
            travel.append(node)
            # 그 노드에 연결되어 있으면서 방문하지 않은 노드를 탐색해서 스택에 push
            for i in AL[node]:
                # if not visited[i]:
                if visited[i] == 0:
                    stack.append(i)
    # DFS의 while을 끝낸 시점
    print(stack)
    print(visited)
    print(tavel)