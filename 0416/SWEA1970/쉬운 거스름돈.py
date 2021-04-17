import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    change = int(input()[:-1]+'0')
    WON = [0]*8
    won = 50000
    i = 0
    while change:
        if change - won >= 0:
            WON[i] += change // won
            change = change - won * (change // won)
        won = won // 2 if i % 2 else won // 5
        i += 1
    print('#%d\n%s' % (t, ' '.join(map(str, WON))))