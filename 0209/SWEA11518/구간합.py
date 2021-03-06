import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    min_sum = float('inf')
    max_sum = 0
    for i in range(n-m+1):
        sum_num = 0
        for j in range(m):
            sum_num += num[i+j]

        if min_sum > sum_num:
            min_sum = sum_num
        if max_sum < sum_num:
            max_sum = sum_num

    ans = max_sum - min_sum
    print('#%d %d' %(t, ans))