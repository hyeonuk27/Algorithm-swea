import sys
sys.stdin = open('input.txt')

# 이진 탐색 함수 정의
def binary(l, r, p, cnt):
    while l <= r:
        m = (l + r) // 2
        cnt += 1
        if m == p:
            return cnt
            break
        elif m > p:
            r = m
        else:
            l = m
    return false

l, cnt_a, cnt_b = 1, 0, 0
for t in range(1, int(input()) + 1):
    r, pa, pb = map(int, input().split())
    # A, B의 cnt 반환
    A = binary(l, r, pa, cnt_a)
    B = binary(l, r, pb, cnt_b)

    # 대소 비교
    if A - B < 0:
        ans = 'A'
    elif A - B > 0:
        ans = 'B'
    else:
        ans = '0'

    print('#%d %s' % (t, ans))