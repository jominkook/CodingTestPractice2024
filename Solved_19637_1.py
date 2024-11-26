import sys
sys.stdin.readline

N,M = map(int, input().split())
arr = []

for i in range(N):
    name,power = input().split()
    arr.append((name,int(power)))
    
for i in range(M):
    
    power = int(input())
    
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start+end)//2
        
        if arr[mid][1] >= power:
            end = mid - 1
        else:
            start = mid + 1
            
    print(arr[start][0])
    
    
    
            
            
    
    


    
    
        
    
            
            
            


    