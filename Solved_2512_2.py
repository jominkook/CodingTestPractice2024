N = int(input())

budget =list(map(int,input().split()))

M = int(input())

start = 0
end = max(budget)


while start <= end:
    mid =(start+end)//2
    
    total = 0
    for i in budget:
        if i > mid:
            total += mid
        else:
            total += i
            
    if total > M:
        end = mid - 1
        
    else:
        start = mid + 1
        
print(end)