#백준 1205번 등수 구하기
# 2번째 풀이
N, NEW_SCORE, P = map(int, input().split())
scores = []
if N == 0 and NEW_SCORE == 0 and P == 0:
    print(1)
    exit()
else:
    scores = list(map(int, input().split()))
    scores.append(NEW_SCORE)
    scores.sort(reverse=True)
    if N == P and scores[-1] >= NEW_SCORE:
        print(-1)
    else:
        print(scores.index(NEW_SCORE) + 1)
        
        

                
          
                
                
    