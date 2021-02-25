import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    customer = sorted(customer) # 가장 늦은 방문 시간을 찾고자 정렬
    last_visit = customer[-1] # 가장 늦은 방문 시간

    # 0초에 고객이 방문하면 무조건 Impossible
    if not customer[0]:
        ans = 'Impossible'
    else:
        remain = 0 # 남아있는 붕어빵
        s = 1 # 1초 ( 0초일 때는 위에서 확인하고 옴)
        c = 0 # 고객 목록 돌리는 idx
        # 1초부터 1초씩 증가한 시간이
        # 가장 늦은 방문 시간과 일치하면 반복문을 종료함
        while s < last_visit + 1:
            # 붕어빵 만드는 시간과 t가 일치할 때
            # remain에 만든 붕어빵 넣는다
            if s % m == 0:
                remain += k

            # 손님이 방문한 시간과 t가 일치할 때
            # 붕어빵이 비었다면, impossible -> break
            # 붕어빵이 있다면, remain에 있는 붕어빵 1개씩 꺼내서 판다
            if s == customer[c]:
                if not remain:
                    ans = 'Impossible'
                    break
                remain -= 1
                c += 1
            # while 종료 조건
            s += 1

        if remain:
            ans = 'Possible'
        else:
            ans = 'Impossible'
    print('#%d %s' % (t, ans))







