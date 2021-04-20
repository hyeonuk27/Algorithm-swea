import sys
sys.stdin = open('input.txt')

def get_sol(lv, cnt, remains):
    global min_cnt
    if cnt >= min_cnt:
        return
    if lv >= N-1:
        min_cnt = cnt
        return
    if remains < charge[lv]:
        get_sol(lv + 1, cnt + 1, charge[lv] - 1)
    if remains:
        get_sol(lv + 1, cnt, remains - 1)


for t in range(1, int(input())+1):
    charge = list(map(int, input().split()))
    N = charge.pop(0)
    min_cnt = 987654321
    get_sol(0, 0 ,0)
    print('#%d %d' % (t, min_cnt - 1))