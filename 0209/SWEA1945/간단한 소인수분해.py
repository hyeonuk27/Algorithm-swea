import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    m = [2, 3, 5, 7, 11]
    ans = [0] * len(m)

    for i in range(len(m)):
        while n % m[i] == 0:
                ans[i] += 1
                n = int(n / m[i])

    print('#{}'.format(t), end=' ')
    for i in ans:
        print(i, end=' ')
    print()