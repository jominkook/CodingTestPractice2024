# 1138 한 줄로 서기

N = int(input())
line = list(map(int, input().split()))

result = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == line[i] and result[j] == 0:
            result[j] = i + 1
            break
        if result[j] == 0:
            cnt += 1
            
for i in result:
    print(i, end = ' ')

