#백준 1446 지름길
# 9번째 풀이
N,D = map(int,input().split())
shortcuts = []
distances = [i for i in range(D+1)]

for _ in range(N):
    s,e,l = map(int,input().split())
    shortcuts.append([s,e,l])
    
for i in range(D+1):
    
    if i > 0:
        distances[i] = min(distances[i],distances[i-1]+1)
    for s,e,l in shortcuts:
        if e > D:
            continue
        if i == s:
            distances[e] = min(distances[e],distances[i]+l)

print(distances[D])