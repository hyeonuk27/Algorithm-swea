N = 4
subset = [0] * N
# subset의 level 위치를 사용할 지(1) 사용하지 않을 지(0)를 결정
def DFS_subset(level, N): # 현 위치 / 종료 조건으로 사용할 것 / 추가 정보(가지치기용, 확산용...)

    # 종료 조건
    if level == N:
        print(subset)
        return

    # 확산(DFS 호출)
    subset[level] = 0  # level 위치 item 사용
    DFS_subset(level+1, N)
    subset[level] = 1  # level 위치 item 사용하지 않음
    DFS_subset(level+1, N)

DFS_subset(0, N)

