p,m = map(int, input().split())

rooms = list()

for i in range(p):
    level,nickname = input().split()
    level = int(level)
    flag = False
    
    
    for j in rooms:
        if len(j) < m and abs(level - j[0][0]) <= 10:
            j.append((level,nickname))
            flag = True
            break
    if not flag:
        rooms.append([(level,nickname)])
        
for i in rooms:
    print('Started!' if len(i) == m else 'Waiting!')
    i.sort(key = lambda x: x[-1])
    for l,n in i:
        print(l,n)
        




    
    
    
    
    
    
    
    

    




                



    
    










                                                                                                              