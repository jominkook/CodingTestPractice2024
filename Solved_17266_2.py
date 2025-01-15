N = int(input())
M = int(input())
light = list(map(int, input().split()))

start = 1
end = N

def is_possible(height):
    last_covered = 0
    for l in light:
        if l - height > last_covered:
            return False
        last_covered = l + height
    return last_covered >= N

while start <= end:
    mid = (start + end) // 2
    if is_possible(mid):
        end = mid - 1
    else:
        start = mid + 1

print(start)