#백준 4963 섬의개수
# 백트래킹(dfs)
# 첫번째 풀이

import sys
sys.setrecursionlimit(10**6)

W, H = map(int, input().split())
graph = [[0] * W for _ in range(H)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
visited = [[False]*W for _ in range(H)]
for i in range(W):
    for j in range(H):
        if W == 0 and H == 0:
            break
        