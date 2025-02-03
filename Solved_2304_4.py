# 백준 2304 창고 다각형
# 4번째 풀이

N = int(input())

max_h = 0
max_idx = 0

arr = [0]*1001

for _ in range(N):
    L,H = map(int,input().split())
    
    arr[L] = H
    
    if H > max_h:
        max_h = H
        max_idx = L
        
res = 0

left = 0
right = 0

for i in range(max_idx+1):
    if arr[i] > left:
        left = arr[i]
    res += left
    
for i in range(1000,max_idx,-1):
    if arr[i] > right:
        right = arr[i]
    res += right
    
print(res)

