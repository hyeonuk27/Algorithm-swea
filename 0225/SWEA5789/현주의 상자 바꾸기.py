import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, q = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(q)]
    box = [0] * (n)

    chk = 1
    while chk <= q:
        for i in lr:
            l, r = i[0], i[1]
            for j in range(l, r + 1):
                box[j-1] = chk
            chk += 1
    print('#%d' % t , end=' ')
    print(*box)
