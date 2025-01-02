import sys
sys.stdin.readline
N,K = map(int,sys.stdin.readline().split())

table = list(sys.stdin.readline().strip())
result = 0

for i in range(N):
    if table[i] == 'P':
        for j in range(max(0,i-K),min(N,i+K+1)):
            if table[j] == 'H':
                table[j] = 'X'
                result += 1
                break
            
print(result)
            
