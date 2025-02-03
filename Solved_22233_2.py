# 백준 22233 가희와 키워드
# 2번째 풀이

N,M = map(int,input().split())
keywords = [input() for _ in range(N)]
keywords.sort(key=lambda x: len(x))

for _ in range(M):
    word = input()
    word_list = word.split(",")
    for key in word_list:
        if key in keywords:
            keywords.remove(key)
    print(len(keywords))
    

            
    
            
            
            
            
            
    