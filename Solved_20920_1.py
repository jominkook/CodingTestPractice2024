import sys
input = sys.stdin.readline
N,M = map(int,input().split())

dic = {}

for i in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
            
dic = sorted(dic.items(), key = lambda x:(-x[1],-len(x[0]),x[0]))

for key in dic:
    print(key[0])
    
    
    