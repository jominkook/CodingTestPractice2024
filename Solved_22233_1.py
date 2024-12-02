import sys
input = sys.stdin.readline

N,M = map(int,input().split())

keyword = set()
for i in range(N):
    keyword.add(input().rstrip())

for j in range(M):
    sentence = input().rstrip().split(',')
    for k in sentence:
        if k in keyword:
            keyword.remove(k)
    print(len(keyword))    
    
        
        

  
    
    
        

    






    
   

    
    


        
    


