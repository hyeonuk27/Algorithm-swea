import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N = int(input())
    times = [tuple(map(int, input().split()))for _ in range(N)]
    times = sorted(times, key=lambda x:x[1])

    cnt, idx = 1, 0
    for i in range(idx+1, N):
        if times[idx][1] <= times[i][0]:
            cnt += 1
            idx = i
    print('#%d %d' % (t, cnt))