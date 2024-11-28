import sys
sys.stdin.readline

N = int(sys.stdin.readline())

budget = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())


start  = 0
end = max(budget)


while start <= end:
    mid = (start + end) // 2
    total = 0
    for b in budget:
        if total < M:
            if total < mid:
                total += b
            else:
                total += mid
    if total > M:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)
            
            
            
        