import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    box = [0] * (n + 1)
    for i in range(n):
        if box[nums[i]] < 1:
            box[nums[i]] += 1

    ans = []
    for j in range(n):
        if box[j] == 1:
            ans += [j]

    print('#%d %d' % (t, ans[k - 1]))