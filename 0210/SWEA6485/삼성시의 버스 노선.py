import sys
sys.stdin = open('input.txt')

for t in range(1, int(input().strip()) + 1)
    bus_route = []
    for i in range(int(input().strip())):
        bus_route += [list(map(int, input().split()))]

    bus_stop_num = []
    for j in range(int(input().strip())):
        bus_stop_num += [int(input().strip())]

    # 버스 정류장 상자 만들기
    bus_stop = [0] * 5001

    # 노선 개수 만큼 상자에 넣기
    for k in range(len(bus_route)):
        for l in range(bus_route[k][0], bus_route[k][1] + 1):
            bus_stop[l] += 1

    # bus_stop_num에 해당하는 노선 개수 출력하기
    print('#{}'.format(t), end=' ')
    for i in range(len(bus_stop_num)):
        print(bus_stop[bus_stop_num[i]], end=' ')
    print()