T = int(input())

for i in range(T):
    n,k,t,m = map(int, input().split())
    
    problems = [[0] * k for _ in range(n)]
    submissions = [0] * n
    time = [0] * n
    
    for _ in range(m):
        i, j, s = map(int, input().split())
        problems[i-1][j-1] = max(problems[i-1][j-1], s)
        submissions[i-1] += 1
        time[i-1] = i

        
    scores = [0] * n
    for i in range(n):
        scores[i] = sum(problems[i])
        
    
    for i in  range(n):
        if i == t-1:
            print(sorted(scores, reverse=True).index(scores[i])+1)
            break
        
            
        
            
        
        
    


            
            
    
        
        
        
        
   
        
        
        
        

            
            
        
        
        
        
        
        
        
        
        
        
        