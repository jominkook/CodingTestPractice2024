N,K = map(int,input().split())

sequence = list(map(int,input().split()))

left = 0
right = 0
result = 0

count = [0] * 100001

while right < N:
    count[sequence[right]] += 1

    if count[sequence[right]] > K:
        result = max(result,right - left)
        while count[sequence[right]] > K:
            count[sequence[left]] -= 1
            left += 1
    right += 1
    
result = max(result,right - left)
print(result)