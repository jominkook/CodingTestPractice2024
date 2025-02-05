# 백준 2304 창고다각형
# 5번째 풀이

N = int(input())

piller = [0] * 1001

rect = []

for _ in range(N):
    L, H = map(int, input().split())
    piller[L] = H

#가장 높은 높이의 기둥을 기준으로 잡음    
max_H = max(piller)
max_idx = piller.index(max_H)

left = 0
right = 0

#왼쪽
for i in range(max_idx):
    if piller[i] > left:
        left = piller[i]
    rect.append(left)
    
#오른쪽
for i in range(1000, max_idx, -1):
    if piller[i] > right:
        right = piller[i]
    rect.append(right)
    
print(sum(rect) + max_H)
    
    