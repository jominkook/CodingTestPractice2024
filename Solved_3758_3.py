#KCPC 문제

T = int(input())


for _ in range(T):

    n,k,t,m = map(int, input().split())
    

    sovled = [[0] * k for _ in range(n)]
    score = [0] * n
    submit = [0] * n
    time = [0] * n

    for _ in range(m):
        i,j,s = map(int, input().split())
        i -= 1
        j -= 1
        sovled[i][j] = max(sovled[i][j], s)
        submit[i] += 1
        
    for i in range(n):
        for j in range(k):
            if sovled[i][j] > 0:
                score[i] += sovled[i][j]
                time[i] += 1
    rank = 1
    for i in range(n):
        if score[i] > score[t-1]:
            rank += 1
        elif score[i] == score[t-1]:
            if time[i] < time[t-1]:
                rank += 1
            elif time[i] == time[t-1]:
                continue                
    print(rank)
                
 
    
  

    
 


    

