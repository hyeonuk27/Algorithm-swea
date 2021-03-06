import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    max_box, min_box = -1, 101
    max_idx, min_idx = 0, 0
    while True:
        for i in range(len(box)):
            if max_box < box[i]:
                max_box = box[i]
                max_idx = i
            if min_box > box[i]:
                min_box = box[i]
                min_idx = i

        if dump == 0 or max_box - min_box <= 1:
            ans = max_box - min_box
            break

        max_box -= 1
        min_box += 1
        dump -= 1
        box[max_idx] = max_box
        box[min_idx] = min_box

    print('#{} {}'.format(t, ans))