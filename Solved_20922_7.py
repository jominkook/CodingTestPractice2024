#백준 20922 겹치는 건 싫어
# 7번째 풀이

N,K = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 0

max_len = 0

num_dict = {}

while right < N:
    if arr[right] in num_dict:
        num_dict[arr[right]] += 1
    else:
        num_dict[arr[right]] = 1
        
    if num_dict[arr[right]] > K:
        max_len = max(max_len,right-left)
        while num_dict[arr[right]] > K:
            num_dict[arr[left]] -= 1
            left += 1
            
    right += 1
    
max_len = max(max_len,right-left)
print(max_len)
    


        
    
    
    
        
    