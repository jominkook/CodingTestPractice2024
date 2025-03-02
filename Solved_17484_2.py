import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1]
answer = float('inf')

def dfs(px, py, pd, cost):
    global answer
    if px == N - 1:
        answer = min(answer, cost)
        return
    for i in range(3):
        if pd == i:  # 이전 방향과 같은 방향으로 이동하지 않음
            continue
        nx = px + 1
        ny = py + dy[i]
        if 0 <= ny < M:
            dfs(nx, ny, i, cost + graph[nx][ny])

for i in range(M):
    dfs(0, i, -1, graph[0][i])

print(answer)