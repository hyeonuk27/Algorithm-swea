import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    A, B = map(int, input().split())

    if abs(A - B) == 2:
        if A > B:
            ans = 'B'
        else:
            ans = 'A'

    elif A - B == 0:
        ans = '='

    else:
        if A > B:
            ans = 'A'
        else:
            ans = 'B'

    print('#{} {}'.format(t, ans))