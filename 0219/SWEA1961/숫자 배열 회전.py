import sys
sys.stdin = open('input.txt')

def rotate_90(arr):
    arr_90 = [[''] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr_90[c][n-1-r] = arr[r][c]
    return arr_90

def rotate_180(arr):
    arr_180 = [[''] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr_180[n-1-r][n-1-c] = arr[r][c]
    return arr_180

def rotate_270(arr):
    arr_270 = [[''] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr_270[n-1-c][r] = arr[r][c]
    return arr_270

for t in range(1, int(input())+1):
    n = int(input())
    arr = [input().split() for _ in range(n)]

    arr_90 = rotate_90(arr)
    arr_180 = rotate_180(arr)
    arr_270 = rotate_270(arr)

    print('#%d' % t)
    for i in range(n):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))





