import sys
sys.stdin = open('input.txt')

# 모든 부분 집합을 만들어 답을 찾아도 된다 -> 확장성!
A = list(range(1, 13))
a = len(A)
lst = []
for i in range(1, 1 << a):
    in_lst = []
    for j in range(a):
        if i & (1 << j):
            in_lst += [A[j]]
    lst += [in_lst]

# n, k 조건 충족하는 부분 집합 개수 반환
for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    ans_lst = [1 for i in lst if len(i) == n if sum(i) == k]
    ans = 0 if len(ans_lst) == 0 else 1

    print('#%d %d' % (t, ans))



