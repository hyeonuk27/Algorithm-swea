import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    # 오븐 크기 만큼 피자 인덱스 넣기
    oven = [i for i in range(n)]
    # 다음 피자 인덱스를 찾기 위해 변수 만들기
    pizza_idx = n

    while len(oven) > 1:
    # 1번 위치에서 피자 꺼낸 후 치즈 확인
    # 녹았다 -> 다음 피자 1번 위치에 넣기
    # 녹지 않았다 -> 화덕 맨 뒤에 넣기
        i = oven.pop(0)
        cheese[i] //= 2
        if cheese[i]> 0:
            oven.append(i)
        elif pizza_idx < m:
            oven.insert(0, pizza_idx)
            pizza_idx += 1
    print('#%d %d' % (t, oven[0] + 1))