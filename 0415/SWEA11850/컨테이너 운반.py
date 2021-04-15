import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    C, T = map(int, input().split())
    containers = sorted(map(int, input().split()), reverse=1)
    trucks = sorted(map(int, input().split()), reverse=1)

    ans = 0
    for i in range(T):
        for j in range(C):
            if trucks[i] >= containers[j]:
                ans += containers[j]
                containers.pop(j)
                C -= 1
                break
    print('#%d %d' % (t, ans))
