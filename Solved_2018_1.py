N = int(input())
start = 1
end = 1
cnt = 1 # 자기 자신
sum = 1

if N == 1 or N == 2:
    print(1)
    exit()
    
while end <= N//2+1:
    if sum == N:
        cnt += 1
        end += 1
        sum += end
    elif sum < N:
        end += 1
        sum += end
    else:
        sum -= start
        start += 1
print(cnt)