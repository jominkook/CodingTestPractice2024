N,K = map(int,input().split())

dp = [0] * 100001

arr = list(map(int,input().split()))

left = 0
right = 0
answer = 0

while right < N:
    dp[arr[right]] += 1
    if dp[arr[right]] > K:
        while dp[arr[right]] > K:
            dp[arr[left]] -= 1
            left += 1
            
    answer = max(answer,right-left+1)
    right += 1
    
    
print(answer)
    
        
