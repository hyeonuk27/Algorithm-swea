import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    nums = list(map(int, input().split()))

    #bubble sort

    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    print('#{} {}'.format(t, nums[-1]))