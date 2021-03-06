import sys
sys.stdin = open('input.txt')


def get_solution(pN, pD):
    # 1. 만약 x가 max(x-2, x-1, x+1, x+2)보다 작다면 조망권 있다
    # 2. 조망권이 확보된 세대 수는 x - max(x-2, x-1, x+1, x+2)
    # 3. 세대 수 합을 return
    house_sum = 0
    for i in range(2, pN-2):
        base = pD[i]
        max_num = 0
        for j in [-2, -1, 1, 2]:
             if max_num < pD[i+j]:
                max_num = pD[i+j]
        if base > max_num:
            house = base - max_num
            house_sum += house
    return house_sum

T = 10
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    ans = get_solution(N, D)
    print('#{} {}'.format(t, ans))