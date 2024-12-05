import sys
from collections import deque


N = int(sys.stdin.readline())

q = deque()

for i in range(N):
    q.extend(list(map(int, sys.stdin.readline().split())))
    q = deque(sorted(q, reverse=True)[:N])
    
print(q[N-1])