import sys
sys.stdin = open('input.txt')

def hamburger(start, score, cal):
    # 종료조건
    global mx
    #if cal > L: return

    if score > mx:
        mx = score

    for i in range(start, N):
        if expect[i] + score <= mx: break  # 가지치기 2 point
        if cal + cals[i] > L: continue     # 가지치기 1
        hamburger(i + 1, score + points[i], cal + cals[i])


T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    points = [a[n][0] for n in range(N)] ## point
    cals = [a[n][1] for n in range(N)] ## point

    # 가지치기 2를 위한 것
    expect = [0] * N
    expect[N-1] = points[N-1]
    for x in range(N-2, -1, -1):
        expect[x] = expect[x+1] + points[x]

    mx = 0
    hamburger(0, 0, 0)
    print("#%d %d" % (t, mx))