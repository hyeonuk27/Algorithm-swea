import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N = input().strip()

    # 상자 만들기
    arr = [0] * 10
    for i in range(len(N)):
        arr[int(N[i])] += 1

    triplet_num = 0
    run_num = 0
    # triple : 상자에 3 이상이 담겨 있을 경우
    for i in range(len(arr)):
        if arr[i] == 3:
            triplet_num += 1
        elif arr[i] == 6:
            triplet_num +=2

    # run : 상자에 연속인 수가 담겨 있을 경우
    for i in range(len(arr)-2):
        if arr[i] == arr[i+1] == arr [i+2] == 1:
            run_num += 1
        elif arr[i] == arr[i+1] == arr [i+2] ==2:
            run_num += 2

    if triplet_num + run_num == 2:
        ans = 'Baby Gin'
    else:
        ans ='Lose'

    print('#{} {}'.format(t, ans))