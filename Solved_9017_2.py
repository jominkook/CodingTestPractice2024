from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    teamNums = list(map(int, input().split()))
    
    team_cnt = defaultdict(int)
    team_dict = defaultdict(list)
    
    for i in teamNums:
        team_cnt[i] += 1
    
    # 팀 번호 필터링: 6명의 선수가 있는 팀만 남김
    teamNums = [x for x in teamNums if team_cnt[x] == 6]
    
    for idx, num in enumerate(teamNums):
        team_dict[num].append(idx)
        
    result = list(team_dict.keys())
    result.sort(key=lambda x: (sum(team_dict[x][:4]), team_dict[x][4], team_dict[x][5]))
    
    print(result[0])