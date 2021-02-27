import sys
sys.stdin = open('input.txt')

alien_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
N = len(alien_num)

for t in range(1, int(input()) + 1):
    tc, n = input().split()
    nums = input().split()
    cnt = [0] * N

    for i in nums:
        for j in range(N):
            if i == alien_num[j]:
                cnt[j] += 1
                break

    ans = ''
    for k in range(N):
        ans += (alien_num[k] + ' ') * cnt[k]

    print(tc)
    print(ans)


