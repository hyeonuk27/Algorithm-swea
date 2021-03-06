import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    box = list(map(int, input().split()))
    # 떨어지는 횟수 담을 상자 만들기
    fall = [0] * (n + 1)

    # 기준 상자가 오른쪽 상자보다 높으면 떨어짐 -> fall +1
    for i in range(len(box)):
        for j in range(i+1, len(box)):
            if box[i] > box[j]:
                fall[i] += 1

    # 최대 낙차 구하기
    max_fall = -1
    for k in range(len(fall)):
        if max_fall < fall[k]:
            max_fall = fall[k]

    print('#%d %d'%(t, max_fall))