#겹치는 건 싫어

N,K = map(int,input().split())

arr = list(map(int,input().split()))

start = 0
end = 0

dic = {}

max_len = 0

while end < N:
    if arr[end] in dic:
        dic[arr[end]] += 1
    else:
        dic[arr[end]] = 1

    if dic[arr[end]] > K:
        max_len = max(max_len,end-start)
        while dic[arr[end]] > K:
            dic[arr[start]] -= 1
            start += 1
    end += 1
    
max_len = max(max_len,end-start)

print(max_len)