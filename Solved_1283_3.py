N = int(input())


keys = []

for i in range(N):
    
    words = list(map(str, input().split()))
    
    for j in range(len(words)):
        if words[i][0].upper() not in keys:
            keys.append(words[i][0].upper())
            words[i] = "[" + words[i][0] + "]" + words[i][1:]
            print(" ".join(words))
            break
    else:
        for j in range(len(words)):
            flag = False
            for k in range(len(words[j])):
                if words[j][k].upper() not in keys:
                    keys.append(words[j][k].upper())
                    flag = True
                    words[j] = words[j][:k] + "[" + words[j][k] + "]" + words[j][k + 1:]
                    print(" ".join(words))
                    break
            if flag:
                break
        else:
            print(*words)
        
    