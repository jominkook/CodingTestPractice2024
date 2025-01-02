import sys
sys.stdin.readline
N,M = map(int,input().split())

char_power = []

for _ in range(N):
    name,power = sys.stdin.readline().split()
    char_power.append((name,int(power)))
    
    
char_power.sort(key = lambda x: x[1])


for _ in range(M):
    start = 0
    end = N-1
    
    power1 = int(sys.stdin.readline())
    
    while start <= end:
        mid = (start + end) // 2
        
        if char_power[mid][1] >= power1:
            end = mid - 1
            
        else:
            start = mid + 1
            
    print(char_power[start][0])