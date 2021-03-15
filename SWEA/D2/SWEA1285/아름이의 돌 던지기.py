import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    rocks = list(map(int, input().split()))

    dis = []
    for rock in rocks:
        dis += [abs(rock-0)]

    min_dis = min(dis)
    people = dis.count(min_dis)

    print('#{} {} {}'.format(t, min_dis, people))