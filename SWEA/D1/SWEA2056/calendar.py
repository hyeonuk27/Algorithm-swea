import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N = input()

    end_dates = [0, 31, 28, 31, 30, 31, 30 ,31, 31, 30, 31, 30, 31]
    end_date = end_dates[int(N[4:6])]

    if int(N[4:6]) > 12 or int(N[4:6]) < 1:
        ans = -1

    elif int(N[-2:]) not in range(1, end_date + 1):
        ans = -1

    else:
        ans = N[:4] + '/' + N[4:6] + '/' + N[-2:]


    print('#{} {}'.format(t, ans))
