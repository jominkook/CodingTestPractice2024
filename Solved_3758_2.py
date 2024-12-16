import sys
sys.stdin.readline

T = int(sys.stdin.readline())

for _ in range(T):
    n,k,t,m = map(int, sys.stdin.readline().split())
    team = [0]*n
    score = [0]*n
    submit = [0]*n
    for _ in range(m):
        i,j,s = map(int, sys.stdin.readline().split())
        i -= 1
        j -= 1
        submit[i] += 1
        if s > score[i]:
            score[i] = s
            team[i] = j
            
    rank = 1
    
    for i in range(n):
        if i == t-1:
            continue
        if score[i] > score[t-1]:
            rank += 1
        elif score[i] == score[t-1] and submit[i] > submit[t-1]:
            rank += 1
        elif score[i] == score[t-1] and submit[i] == submit[t-1] and team[i] < team[t-1]:
            rank += 1
    print(rank)

        
        