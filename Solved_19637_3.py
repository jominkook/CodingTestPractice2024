import sys
sys.stdin.readline

N,M = map(int, sys.stdin.readline().split())




for i in range(N):
    name, power = sys.stdin.readline().split()
    power = int(power)
    if i == 0:
        power_list = [[name, power]]
    else:
        power_list.append([name, power])
        


for i in range(M):
    char_power = int(sys.stdin.readline())
    start = 0
    end = N-1
    
    while start <= end:
        mid = (start+end)//2
        if power_list[mid][1] < char_power:
            start = mid + 1
        else:
            end = mid - 1
    print(power_list[start][0])
  
    
    