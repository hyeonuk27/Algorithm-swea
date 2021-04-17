import sys
sys.stdin = open('input.txt')

drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def get_check():
    for cr in range(N):
        for cc in range(N):
            for dr, dc in drc:
                nr, nc = cr + dr, cc + dc
                if -1 < nr < N and -1 < nc < N and room[cr][cc] +1 == room[nr][nc]:
                    check[room[nr][nc]] = 1


def get_max_cnt():
    max_cnt = cnt = idx = 0
    for i in range(len(check)-1, -1, -1):
        if check[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                idx = i + 1
            cnt = 0
    return idx - 1, max_cnt + 1


for t in range(1, int(input())+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N * (N+1)
    get_check()
    idx, max_cnt = get_max_cnt()
    print('#%d %d %d' % (t, idx, max_cnt))