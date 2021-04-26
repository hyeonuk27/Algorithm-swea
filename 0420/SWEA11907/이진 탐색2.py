import sys
sys.stdin = open('input.txt')

def binary_search(num):
    left, right, status = 0, N-1, 0
    while left <= right:
        m = (left + right) // 2
        if A[m] == num:
            return 1
        if A[m] < num:
            if status == 1:
                return 0
            left = m + 1
            status = 1
        else:
            if status == -1:
                return 0
            right = m - 1
            status = 0

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for num in B:
        if binary_search(num):
            ans += 1
    print('#%d %d' % (t, ans))