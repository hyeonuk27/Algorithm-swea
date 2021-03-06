import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    num = input()
    cnt = [0] * 10

    # cnt 상자 채우기
    for i in range(len(num)):
        cnt[int(num[i])] += 1

    # 가장 큰 수와, idx 찾
    max_num = -1
    max_num_idx = -1
    for i in range(len(cnt)):
        if max_num <= cnt[i]:
            max_num = cnt[i]
            max_num_idx = i

    print('#%d %d %d' % (t, max_num_idx, max_num))