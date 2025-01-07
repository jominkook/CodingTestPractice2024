#백준 1522_2
#잘못된방법

S = input()

length = len(S)
visited = [False] * length

def bfs(start, end):
    global visited
    queue = [start]
    visited[start] = True
    while queue:
        x = queue.pop(0)
        for i in range(length):
            if not visited[i] and S[x] != S[i]:
                visited[i] = True
                queue.append(i)
    return visited[end]

answer = 0

for i in range(length):
    if not visited[i]:
        answer += 1
        if bfs(i, (i + length) % length):
            answer -= 1
            
print(answer)
    