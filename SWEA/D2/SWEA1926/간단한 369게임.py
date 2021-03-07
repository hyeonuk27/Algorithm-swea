import sys
sys.stdin = open('input.txt')

N = int(input())
# 1~N까지의 한정된 범위 내에서의 반복 -> for
for n in range(1, N+1):
    num = n
    cnt = 0 # 3, 6, 9 개수

    # 10으로 나누어 몫이 점점 작아지다가 그 값이 0이 되면 종료 -> while문
    while num > 0:
        d = num % 10
        num = int(num/10)  # 종료 조건
        if d == 3 or d == 6 or d == 9:
            cnt += 1
    if cnt == 0:
        print(n, end=' ')
    else:
        print('-' * cnt, end=' ')