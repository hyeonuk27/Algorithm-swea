import sys
sys.stdin = open('input.txt')

def game(arr, num):
    arr[num] += 1
    if arr[num] >= 3:
        return 1
    for i in range(8):
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            return 1
    return 0

def get_sol():
    player1 = [0] * 10
    player2 = [0] * 10
    for num1, num2 in zip(cards[::2], cards[1::2]):
        if game(player1, num1):
            return 1
        if game(player2, num2):
            return 2
    return 0

for t in range(1, int(input())+1):
    cards =  list(map(int, input().split()))
    print('#%d %d' % (t, get_sol()))