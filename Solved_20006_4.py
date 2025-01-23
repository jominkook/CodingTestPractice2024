P,M = map(int, input().split())
rooms = []
for i in range(P):
    level,nic = input().split()
    level = int(level)
    rooms.append([level,nic])
    flag = False
    
    for room in rooms:
        key = rooms[0][0]

        if key - 10 <= level <= key + 10 and len(room) < M:
            room.append((level,nic))
            flag = True
            break
    if not flag:
        rooms.append([(level,nic)])
        
for room in rooms:
    if len(room) == M:
        print('Started!')
    else:
        print('Waiting!')
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)