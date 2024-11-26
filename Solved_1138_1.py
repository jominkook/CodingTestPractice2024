import sys
sys.stdin.readline

N = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))

line = [0] * N

for i in range(N):
    count = people[i]
    for j in range(N):
        if count == 0 and line[j] == 0:
            line[j] = i + 1
            break
        elif line[j] == 0:
            count -= 1
            
print(*line)
    


    
    
