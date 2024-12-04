import sys

T  = int(sys.stdin.readline())

for i in range(T):
    n,k,t,l = map(int, sys.stdin.readline().split())
    score = [[0] for _ in range(k)]
    submit = [0 for _ in range(n)]
    time = [0 for _ in range(n)]
    
    for k in range(l):
        i,j,s = map(int, sys.stdin.readline().split())
        score[i-1][j-1] = max(score[i-1][j-1], s)
        submit[i-1] += 1
        time[i-1] = k
        
    rank = []
    
    for h in range(n):
        rank.append((sum(score[h]), submit[h], time[h], h))
        
    rank.sort(key = lambda x: (-x[0], x[1], x[2]))
    
    for r in range(n):
        if rank[r][3] == t-1:
            print(r+1)
            break
        
           