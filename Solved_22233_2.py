# 백준 22233 가희와 키워드
# 2번째 풀이
# 시간초과
import sys
sys.stdin.readline
N,M = map(int,sys.stdin.readline().split())

keywords = []
for _ in range(N):
    keywords.append(sys.stdin.readline().strip())
    
for _ in range(M):
    word = sys.stdin.readline().strip()
    word_list = word.split(",")
    for key in word_list:
        if key in keywords:
            keywords.remove(key)
    print(len(keywords))
    

            
    
            
            
            
            
            
    