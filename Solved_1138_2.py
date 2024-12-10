import sys
input = sys.stdin.readline


N = int(input())

people = list(map(int, input().split()))

order = [0] * N

for i in range(N):
    count = 0
    for j in range(N):
        if count == people[i] and order[j] == 0:
            order[j] = i + 1
            break
        if order[j] == 0:
            count += 1
            
print(*order)
    
    