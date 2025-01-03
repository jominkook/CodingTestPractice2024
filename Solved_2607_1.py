#2607 비슷한 단어
import sys
sys.stdin.readline

N = int(input())
target = list(input())

result = 0  

for i in range(N-1):
    word = list(input())
    temp = target.copy()
    cnt = 0
    for j in range(len(word)):
        if word[j] in temp:
            temp.remove(word[j])
        else:
            cnt += 1
    if cnt == 1 or cnt == 0 and abs(len(word) - len(target)) == 1:
        result += 1
print(result)
 

