import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    N, M = input(), input()
    n, m = len(N), len(M)

    for i in range(m - n + 1):
        cnt = 0
        for j in range(n):
            if M[i+j] == N[j]:
               cnt +=1
            else:
                break
        if cnt == n:
            ans = 1
            break
        else:
            ans = 0

    print('#%d %d' % (t, ans))