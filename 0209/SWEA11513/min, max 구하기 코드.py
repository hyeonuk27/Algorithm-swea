import sys
sys.stdin = open('input.txt')

def get_solution(n, d):

    max_num = d[0]
    min_num = d[0]
    for i in range(n):
        if max_num < d[i]:
            max_num = d[i]
        elif min_num > d[i]:
            min_num = d[i]
    return max_num - min_num

T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    ans = get_solution(N, D)
    print('#%d %d' %(t, ans))