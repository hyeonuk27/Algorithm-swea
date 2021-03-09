import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    num = int(input())
    nums = set()
    n = 0
    while len(nums) < 10:
        n += 1
        temp = num * n
        while temp > 0:
            nums.add(temp % 10)
            temp //= 10
    print('#%d %d' % (t, n*num))