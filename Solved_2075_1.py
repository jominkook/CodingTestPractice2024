import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]   
for i in range(N):
    arr[i].sort()
    arr[i].reverse()
    
result = []

for i in range(N):
    for j in range(N):
        result.append(arr[j][i])
        
result.sort(reverse=True)
print(result[N-1])


    





            

    



        

        
        
        
        

        



        
    
    
           

                                                              



        
    
    