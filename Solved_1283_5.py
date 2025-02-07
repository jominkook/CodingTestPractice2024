#백준 1283 단축키 지정
# 5번째 풀이

N = int(input())

shortkeys = []

for _ in range(N):
    word = list(input().split())
    
    for i in range(len(word)):
        if word[i][0].upper() not in shortkeys:
            shortkeys.append(word[i][0].upper())
            word[i] = "[" + word[i][0] + "]" + word[i][1:]
            print(" ".join(word))
            break
    #break가 실행되지 않았을 때 else문 실행
    else:
        for j in range(len(word)):
            flag = False
            for k in range(len(word[j])):
                if word[j][k].upper() not in shortkeys:
                    shortkeys.append(word[j][k].upper())
                    flag = True
                    word[j] = word[j][:k] + "[" + word[j][k] + "]" + word[j][k + 1:]
                    print(" ".join(word))
                    break
            if flag:
                break
        else:
            print(*word)
    

    
    
    

