import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    str1 = str(set(input()))
    str2 = input()
    n = len(str1)
    cnt = [0] * n

    for i in str2:
        max_cnt = 0
        for j in range(n):
            if i == str1[j]:
                cnt[j] += 1
            if max_cnt < cnt[j]:
                max_cnt = cnt[j]

    print( '#%d %d' % (t, max_cnt))