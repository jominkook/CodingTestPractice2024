import sys
sys.stdin.readline

N = int(input())
word = str(input())
target = []
for i in range(N-1):
    target.append(str(input()))
    
answer = 0

for i in range(N-1):
    if len(word) != len(set(target[i])):
        continue
    
    if len(word) == len(set(target[i])):
        for j in range(len(word)):
            if word[j] in target[i]:
                continue
            else:
                break
        else:
            answer += 1
            
print(answer)

