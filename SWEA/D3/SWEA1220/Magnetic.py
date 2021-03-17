import sys
sys.stdin = open('input.txt')

def get_deadlock(table, n):
    cnt = 0
    for i in range(n):
        for j in range(n-1):
            if table[j][i] == 1:
                if table[j+1][i] == 2:
                    cnt += 1
                else :
                    table[j+1][i] = 1
    return cnt

for t in range(1, 11):
    n =  int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    ans = get_deadlock(table, n)
    print('#%d %d' % (t, ans))


