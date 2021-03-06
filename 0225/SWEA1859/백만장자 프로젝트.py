import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    price = list(map(int, input().split()))

    profit, max_price = 0, 0
    for i in range(n-1, -1, -1): # 뒤에서부터 반복문 돌리기
        # max_price 갱신
        if max_price < price[i]:
            max_price = price[i]
        # max_price >= price일 때, profit 갱신
        else:
            profit += max_price - price[i]

    print('#%d %d' % (t, profit))