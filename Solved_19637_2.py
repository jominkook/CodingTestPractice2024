import sys
sys.stdin.readline

N,M = map(int, sys.stdin.readline().split())
characters = []
for i in range(N):
    name, power = sys.stdin.readline().split()
    characters.append((name, int(power)))
    



for i in range(M):
        
    start = 0
    end = N - 1
    char_power = int(sys.stdin.readline().rstrip())
    
    while start <= end:
        mid = (start + end) // 2
        
        if characters[mid][1] >= char_power:
            end = mid - 1
        else:
            start = mid + 1
            
    print(characters[start][0])
            
            
            

        

    

            



                

        
    

    

    
   
    
        
        
        
        
        
        
    