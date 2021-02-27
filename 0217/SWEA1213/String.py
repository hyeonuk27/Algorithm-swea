import sys
sys.stdin = open('input.txt')

for t in range(10):
    tc = int(input())
    part, full = input(), input()
    p, f = len(part), len(full)

    ans = 0
    # 범위 : 0 ~ f - p
    for i in range(f - p + 1):
        cnt = 0
        for j in range(p):
            if full[i + j] == part[j]:
                cnt += 1
            else:
                break
        if cnt == p:
            ans += 1

    print('#%d %d' % (tc, ans))

