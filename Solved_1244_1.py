#백준 1244 스위치 켜고 끄기
# 첫번째 풀이
N = int(input())
switch = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    sex,num = map(int, input().split())
    if(sex == 1):
        for i in range(num-1,N,num):
            switch[i] = 1 - switch[i]
    if(sex == 2):
        num = num - 1
        for i in range(1,N):
            if(0<=num-i and num+i<N and switch[num-i] == switch[num+i]):
                switch[num-i] = 1 - switch[num-i]
                switch[num+i] = 1 - switch[num+i]
            if(0<=num-i and num+i<N and switch[num-i] != switch[num+i]):
                break
        switch[num] = 1 - switch[num]
                
for i in range(0,N,20):
    print(*switch[i:i+20])