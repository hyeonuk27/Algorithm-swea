import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    t = int(input())
    scores = list(map(int, input().split()))

    box = [0] * 101
    for i in range(len(scores)):
        box[scores[i]] += 1

    max_N = 0
    max_N_idx = 0
    for i in range(len(box)):
        if max_N <= box[i]:
            max_N = box[i]
            max_N_idx = i

    print('#{} {}'.format(t, max_N_idx))