import sys
sys.stdin.readline
N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    arr[i].sort()
    arr[i].reverse()

res = []

for i in range(N):
    for j in range(N):
        res.append(arr[j][i])
        
res.sort(reverse=True)
print(res[N-1])
    