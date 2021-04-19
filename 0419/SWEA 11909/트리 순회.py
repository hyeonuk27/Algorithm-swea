import sys
sys.stdin = open('input.txt')

def preorder(n):
    previsit.append(n)
    if len(tree[n]):
        preorder(tree[n][0])
    if len(tree[n]) == 2:
        preorder(tree[n][1])


def inorder(n):
    if len(tree[n]):
        inorder(tree[n][0])
    invisit.append(n)
    if len(tree[n]) == 2:
        inorder(tree[n][1])


def postorder(n):
    if len(tree[n]):
        postorder(tree[n][0])
    if len(tree[n]) == 2:
        postorder(tree[n][1])
    postvisit.append(n)


for t in range(1, int(input())+1):
    V = int(input())
    nums = list(map(int, input().split()))
    tree = [[] for i in range(V+2)]
    for i in range(len(nums)//2):
        tree[nums[2*i]].append(nums[2*i+1])

    previsit, invisit, postvisit = [], [], []
    preorder(1)
    inorder(1)
    postorder(1)
    ans1 = '-'.join(map(str, previsit))
    ans2 = '-'.join(map(str, invisit))
    ans3 = '-'.join(map(str, postvisit))
    print('#%d\n%s\n%s\n%s' % (t, ans1, ans2, ans3))