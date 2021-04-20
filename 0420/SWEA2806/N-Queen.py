import sys
sys.stdin = open('input.txt')

def N_Queen(lv):
    global cnt
    if lv == N:
        cnt += 1
        return
    for r in range(N):
        if C[r] or D1[r+lv] or D2[r-lv]: continue
        C[r], D1[r+lv], D2[r-lv] = 1, 1, 1
        N_Queen(lv + 1)
        C[r], D1[r+lv], D2[r-lv] = 0, 0, 0

for t in range(1, int(input())+1):
    N = int(input())
    C, D1, D2 = [0] * N, [0] * 2 * N, [0] * 2 * N
    cnt = 0
    N_Queen(0)
    print('#%d %d' %(t, cnt))
