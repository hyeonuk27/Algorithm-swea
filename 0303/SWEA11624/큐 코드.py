import sys
sys.stdin = open('input.txt')

def enQueue(Q, item):
    global rear
    if rear == N - 1 :
        print('Queue_Full')
    else:
        rear += 1
        Q[rear] = item[rear]

def deQueue(Q):
    global front
    global rear
    if rear == front:
        print('Queue_Empty')
    else:
        front += 1
        return Q[front]

t = int(input())
item = input().split()
N = 4
Q = [0] * N
front = -1
rear = -1

enQueue(Q, item)
enQueue(Q, item)
enQueue(Q, item)
a = deQueue(Q)
b = deQueue(Q)
c = deQueue(Q)

print('#%d %s %s %s ' % (t, a, b, c))