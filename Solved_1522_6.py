#백준 1522

S = input()
A = S.count('a')
S = S + S[0:A]

answer = 0

for i in range(len(S)-(A-1)):
    answer = max(answer, S[i:i+A].count('b'))
    
print(A-answer)
        