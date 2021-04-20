import sys
sys.stdin = open('input.txt')

def binary_search(num):
    l, r, direction = 0, N-1, 0
    while l <= r:
        m = (l + r) // 2
        if A[m] == num:
            return 1
        if A[m] < num:
            if direction == 1:
                return 0
            direction = 1
            l = m + 1
        else:
            if direction == -1:
                return 0
            direction = -1
            r = m - 1


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        if binary_search(num):
            cnt += 1
    print('#%d %d' % (t, cnt))