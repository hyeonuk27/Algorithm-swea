import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))

# 버블 정렬 nums를 오름차순 정렬!
for i in range(len(nums)-1, 0, -1):
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

# 중간 위치의 인덱스 찾기

mid_idx = int(len(nums)/2)

# 출력
print(nums[mid_idx])

