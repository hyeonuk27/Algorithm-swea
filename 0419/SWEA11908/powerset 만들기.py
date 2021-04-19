# status[level] = 0
# func(level+1, c_sum)
import sys
sys.stdin = open('input.txt')

def get_powerset(level, S):
    global cnt
    if level >= N:
        if S == M:
            cnt += 1
        return
    status[level] = 1
    get_powerset(level+1, S + nums[level])
    status[level] = 0
    get_powerset(level+1, S)


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    status = [0] * N
    cnt = 0
    get_powerset(0, 0)
    print('#%d %d' %(t, cnt))