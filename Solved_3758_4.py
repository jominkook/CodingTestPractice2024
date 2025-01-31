# 백준 3758번 KCPC
# 4번째 풀이

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    rankingBoard = []
    
    #초기화
    for i in range(n):
        rankingBoard.append([0, 0, [0 for _ in range(k)]])
    
    for time in range(m):
        i,j,s = map(int, input().split())
        rankingBoard[i-1][0] += 1
        rankingBoard[i-1][1] = time
        rankingBoard[i-1][2][j-1] = max(s,rankingBoard[i-1][2][j-1])
        
    sumScore = [0] * n
    for id in range(n):
        sumScore[id] = sum(rankingBoard[id][2])
        
        
    #등수 계산
    
    me = 1
    for team in range(n):
        if team + 1 == t:
            continue
        else:
            if sumScore[team] > sumScore[t-1]:
                me += 1
            elif sumScore[team] == sumScore[t-1]:
                if rankingBoard[team][0] < rankingBoard[t-1][0]:
                    me += 1
                elif rankingBoard[team][0] == rankingBoard[t-1][0]:
                    if rankingBoard[team][1] < rankingBoard[t-1][1]:
                        me += 1
                        
                        
                
                    
    print(me)
 