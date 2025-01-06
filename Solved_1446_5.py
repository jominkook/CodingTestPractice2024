#1446 백준 지름길

import sys
input = sys.stdin.readline

N, D = map(int, input().split())

shortcut = []

for i in range(N):
    s, e, l = map(int, input().split())
    shortcut.append([s, e, l])
    
    
def bfs(D, shortcut):
    distance = [i for i in range(D + 1)]
    
    for i in range(D + 1):
        if i > 0:
            distance[i] = min(distance[i], distance[i - 1] + 1)
            
        for s, e, l in shortcut:
            if i == s and e <= D:
                distance[e] = min(distance[e], distance[i] + l)
                
    return distance[D]

print(bfs(D, shortcut))
        