import sys
sys.stdin = open('input.txt')

def insert(idx, node):
    tree[idx] = node
    # 부모 노드 > 자식 노드
    while tree[idx//2] > tree[idx]:
        # 부모 노드, 자식 노드 위치 교환
        tree[idx//2], tree[idx] =  tree[idx], tree[idx//2]
        # 현 위치보다 한 레벨 위로 이동
        idx //= 2
    return

for t in range(1, int(input())+1):
    N = int(input())
    nodes = list(map(int, input().split()))
    tree = [0] * (N + 1)
    for i in range(N):
        insert(i+1, nodes[i])

    ans = 0
    while N != 1:
        ans += tree[N//2]
        N //= 2
    print("#%d %d" %(t, ans))