import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())

    room = [0] * 201
    for _ in range(n):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        if s % 2:
            s += 1
        if e % 2:
            e += 1
        for i in range(s//2, e//2+1):
            room[i] += 1

    max_num = 0
    for i in room:
        if max_num < i:
            max_num = i

    print('#%d %d' % (t, max_num))