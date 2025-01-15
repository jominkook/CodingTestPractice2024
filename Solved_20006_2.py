
p,m = map(int, input().split())

rooms = []

for _ in range(p):
    l,n = input().split()
    l = int(l)
    flag = False
    for room in rooms:
        key =room[0][0]
        if key - 10 <= l <= key + 10:
            room.append((l,n))
            flag = True
            break
    if not flag:
        rooms.append([(l,n)])
        
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for player in sorted(room, key=lambda x: x[1]):
        print(*player)
        
        
# Solved!
