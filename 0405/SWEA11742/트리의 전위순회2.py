import sys
sys.stdin = open('input.txt')

def preorder(node):
    travel.append(node)
    if tree[node]:
        preorder(tree[node][0])
    if len(tree[node]) == 2:
        preorder(tree[node][1])

V = int(input())
tree = [[] for _ in range(V+1)]
nums = list(map(int, input().split()))
for i in range(0, V*2-2, 2):
    tree[nums[i]].append(nums[i+1])

travel = []
preorder(1)
ans = '-'.join(map(str, travel))
print(ans)