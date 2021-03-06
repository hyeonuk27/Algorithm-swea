import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    price = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * len(won)

    for i in range(len(won)):
        if price // won[i] != 0:
            cnt[i] += price // won[i]
            price = price % won[i]

    print('#{}'.format(t))
    for i in cnt:
        print(i, end =' ')
    print()