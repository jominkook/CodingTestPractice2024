N = int(input())

keys = []

for i in range(N):
    words = list(str,input().split())
    
    
    for j in range(len(words)):
        if words[j][0].upper() not in keys:
            keys.append(words[j][0].upper())
            
        print(keys)
        
        for j in range(len(words)):
            flag = False
            for k in range(len(words)):
                if words[k][0].upper() == keys[j]:
                    flag = True
                    words[k] = "[" + words[k][0] + "]" + words[k][1:]
                    
                    print(" ".join(words))
                    
                    break
                
            if flag:
                break
            
        else:
            print(*words)
    
 
        
    
    
  