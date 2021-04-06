root = [0, 0, 0]  # dummy

def inorder(node):
    if not node:
        return
    inorder(node[1])
    answer.append(str(node[0]))
    inorder(node[2])

def preorder(node):
    if not node:
        return
    answer.append(str(node[0]))
    preorder(node[1])
    preorder(node[2])

def bt_search(x):
    parent = root  # root = [0, 0, 0]
    curr = root  # curr = [0, 0, 0]
    while curr:
        if x == curr[0]:
            break
        parent = curr
        curr = curr[1] if x < curr[0] else curr[2]  # curr = 0
    return parent, curr  # [0, 0, 0], [0,0,0],   [9, 0, 0], 0   일 수 있기 때문에

def bt_insert(x):
    parent, curr = bt_search(x)  # 부모노드, 탐색노드 가져오기
    if type(curr) is list and curr[0] == x:  # 조건 변경
        print('the value %d is already exist' % (x))
        return

    lr_child = 1 if x < parent[0] else 2
    parent[lr_child] = [x, 0, 0]

N = int(input())  # map(int, input().split())
n_node = list(map(int, input().split()))

for value in n_node:
    bt_insert(value)

answer = []
preorder(root[2])
print('-'.join(answer))