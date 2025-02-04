#백준 1138 한줄로서기
# 5번째 풀이

N = int(input())

people = list(map(int, input().split()))

line = [0] * N

for i in range(N):
    cnt = people[i]
    for j in range(N):
        if cnt == 0 and line[j] == 0:
            line[j] = i + 1
            break
        if line[j] == 0:
            cnt -= 1
            
print(*line)