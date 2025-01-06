#백준 2607 비슷한단어

N = int(input())

target = list(input())

result = 0
diff = 0

for i in range(N-1):
    word = list(input())
    diff = 0
    for j in target:
        if j in word:
            word.remove(j)
        else:
            diff += 1
            
    if diff < 2 and len(word) <2:
        result += 1
        
print(result)