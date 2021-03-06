import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    cnt = 0 # 충전 횟수
    bus = 0 # 버스 위치

    # 버스 위치가 n-k+1(8)보다 크면 stop!
    # bus + k 위치로 이동했을 때, 충전소 여부 확인
    # 충전소 없으면 한 칸씩 뒤로 이동하면서 충전소 있는지 확인
    # 충전소 있으면 버스 위치 수정/ 충전 횟수 +1
    # 충전소 없으면 0 출력
    while bus < n-k+1:
        for i in range(k, 0, -1):
            if bus + i in charge:
                cnt += 1
                bus += k
                break
        else:
            cnt = 0
            break
    print('#%d %d'%(t, cnt))