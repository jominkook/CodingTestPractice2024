N,K = map(int,input().split())
table = list(input())
cnt = 0
for i in range(N):
    if table[i] == 'P':
        for j in range(i-K,i+K+1):
            if 0 <= j < N and table[j] == 'H':
                table[j] = 'X'
                cnt += 1
                break
print(cnt)