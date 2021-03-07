import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    time = list(map(int, input().split()))

    h = m = 0
    for i in range(len(time)):
         if i % 2:
             m += time[i]
         else:
             h += time[i]

    if (h + m // 60) % 12 == 0:
        h = 12
    else:
        h = (h + m // 60) % 12
    m = m % 60

    print('#{} {} {}'.format(t, h, m))