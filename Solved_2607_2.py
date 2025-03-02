N = int(input())
words = [input() for _ in range(N)]
target = list(words[0])
answer = 0
for i in range(1, N):
    word = list(words[i])
    diff = 0
    for j in target:
        if j in word:
            word.remove(j)
        else:
            diff += 1
    if diff < 2 and len(word) < 2:
        answer += 1
print(answer)

            

    