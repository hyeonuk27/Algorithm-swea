import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    t = int(input())
    scores = list(map(int, input().split()))

    # 점수 상자 만들기
    box = [0] * 101

    # 점수 상자에 점수 개수 넣기
    for i in range(len(scores)):
        box[scores[i]] += 1


    # 개수 중 가장 큰 수 찾기(index)
    max_N = 0
    max_N_idx = 0
    for i in range(len(box)):
        if max_N <= box[i]:
            max_N = box[i]
            max_N_idx = i


    print('#{} {}'.format(t, max_N_idx))
