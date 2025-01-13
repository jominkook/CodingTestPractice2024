N = int(input())

pliller = [0] * 1001

for _ in range(N):
    L, H = map(int, input().split())
    pliller[L] = H
    
max_h = max(pliller)
max_idx = pliller.index(max_h)

left = pliller[:max_idx]
right = pliller[max_idx+1:]

result = 0

for i in range(len(left)-1):
    if left[i] > left[i+1]:
        left[i+1] = left[i]
   
for i in range(len(right)-1, 0, -1):
    if right[i] > right[i-1]:
        right[i-1] = right[i]
              
result = sum(left) + sum(right) + max_h

print(result)
    