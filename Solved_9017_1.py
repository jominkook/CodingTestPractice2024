from collections import Counter

T = int(input())

for i in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    
    team_limit = []
    
    for key,value in Counter(teams).items():
        if value >= 6:
            team_limit.append(key)
            
    scores = [team for team in teams if team in team_limit]
    counter = {}
        
    for idx,score in enumerate(scores,start = 1):
        if score not in counter:
            counter[score] = [idx,[idx]]
        else:
            counter[score][1].append(idx)
            if len(counter[score][1]) <5:
                counter[score][0] += idx
    winner = None
    min_sum_score = min([counter[key][0] for key in counter.keys()])
    min_5_score = 1001
    for key,value in counter.items():
        if len(value[1]) == 6:
            if value[0] == min_sum_score:
                if min_5_score > value[1][4]:
                    winner = key
                    min_5_score = value[1][4]
    print(winner)
                