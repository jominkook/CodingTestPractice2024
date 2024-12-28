#겹치는건 싫어
#20922번

N,K = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = 0

max_len = 0
cnt = [0] * 100001

while right < N:
    if cnt[arr[right]] < K:
        cnt[arr[right]] += 1
        right += 1
        max_len = max(max_len, right - left)
    else:
        cnt[arr[left]] -= 1
        left += 1
        
print(max_len)