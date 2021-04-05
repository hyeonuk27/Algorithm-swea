import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n > 0:
        travel.append(n)
        preorder(left[n])
        preorder(right[n])

V = int(input())
edge = list(map(int, input().split()))
left = [0] * (V + 1)
right = [0] * (V + 1)

for i in range(V-1):
    n1, n2 = edge[i*2], edge[i*2+1]
    if left[n1] == 0:
        left[n1] = n2
    else:
        right[n1] = n2

travel = []
preorder(1)
ans = '-'.join(map(str, travel))
print(ans)