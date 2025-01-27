# 백준 20006번 
# 5번째 풀이
p,m = map(int,input().split())
rooms = []

for i in range(p):
    level,id = input().split()
    level = int(level)
    flag = False
    for room in rooms:
        key = room[0][0]
        if key- 10 <= level <= key + 10 and len(room) < m:
            room.append((level,id))
            flag = True
            break
    if not flag:
        rooms.append([(level,id)])
        

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)
        
        
      