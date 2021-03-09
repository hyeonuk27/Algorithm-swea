import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    n = int(input())
    t = 1 # 시간
    d = 0 # 거리
    s = 0 # 초기 속도
    for _ in range(n):
        command = list(map(int, input().split()))
        c = command[0]
        if c == 1:
            s = s + command[1]
            d += t * s
        elif c == 2:
            if s >= command[1]:
                s = s - command[1]
                d += t * s
            else:
                d += 0
        else:
            d += t * s
    print('#%d %d' % (tc, d))