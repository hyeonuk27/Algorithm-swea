import sys
sys.stdin = open('input.txt')

# 좋은 답안
for t in range(1, int(input()) + 1):
    numbers, N = input().split()
    length = len(numbers)
    cases = {numbers}
    # N번 교환
    for _ in range(int(N)):
        changed = set()
        for case in cases:
            a = list(case)
            # 조합
            for i in range(length):
                for j in range(i + 1, length):
                    a[i], a[j] = a[j], a[i]
                    changed.add(''.join(a))
                    a[j], a[i] = a[i], a[j]
        cases = changed
    print('#%d %d' % (t, max(map(int, cases))))


# 처음 작성한 코드안(오류)
# for t in range(1, int(input())+1):
#     amount, N = input().split()
#     amount, N = list(amount), int(N)
#     L = len(amount)
#     n = min(L, N)
#     i = j = 0
#     # i값과 max값을 비교함
#     while i < n+j and i != L:
#         j = 0
#         maxnum = max(amount[i::])
#         k = L - amount[::-1].index(maxnum) - 1
#         if amount[i] < amount[k]:
#             amount[i], amount[k] = amount[k], amount[i]
#         # 만약 i값과 max값이 같다면(2번 케이스) i값과 다음 max값을 비교함
#         elif amount[i] == amount[k]:
#             j+=1
#         i+=1
#
#     # 0번 인덱스부터 max값과 비교했기 때문에, 역순으로 n개 만큼이 내림차순인지 확인해야 함(4번 케이스)
#     for m in range(-1, -n, -1):
#         if amount[m] > amount[m-1]:
#             amount[m], amount[m-1] = amount[m-1], amount[m]
#
#     # N이 L보다 크면 그 차이만큼 어떤 값이던 간에 교환을 해줘야 함(10번 케이스)
#     if N > L and (N - L) % 2 == 0:
#         amount[-1], amount[-2] = amount[-2], amount[-1]
#     print('#%d %s' % (t, ''.join(map(str, amount))))