import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N = int(input())
    nums = list(input().split())

    # 최대값 구하기
    max_num = 0
    for i in range(len(nums)):
        if max_num < int(nums[i][0]):
            max_num = int(nums[i][0])

    # 최대값만큼 상자 만들기
    cnt = [0] * (max_num + 1)
    # cnt 상자 채우기
    for i in range(len(nums)):
        cnt[int(nums[i][0])] += 1

    # 누적합 구하기
    for j in range(1, len(cnt)):
        cnt[j] += cnt[j-1]

    # 정렬 결과 넣을 상자 만들기
    ans = [''] * len(nums)
    # cnt 하나씩 깎아서 정답 상자에 넣기
    for k in range(len(nums)-1, -1, -1):
        cnt[int(nums[k][0])] -= 1
        ans[cnt[int(nums[k][0])]] += nums[k]

    print('#%d' % t, end= ' ')
    for i in ans:
        print(i, end=' ')