#백준 1522번 문제: 문자열 교환 a를 b로 바꾸는 최소 횟수

S = input()

length = len(S)

# 문자열을 두 번 이어붙인다.
S = S + S

# 문자열의 길이가 2배인 문자열을 만들어준다.
dp = [[0] * length * 2 for _ in range(length * 2)]

# 문자열의 길이가 1인 경우
for i in range(length * 2):
    if S[i] == 'a':
        dp[i][i] = 1
        
# 문자열의 길이가 2인 경우
for i in range(length * 2 - 1):
    if S[i] == 'a' and S[i + 1] == 'b':
        dp[i][i + 1] = 1
        
# 문자열의 길이가 3 이상인 경우
for i in range(2, length * 2):
    for j in range(length * 2 - i):
        if S[j] == 'a' and S[j + i] == 'b':
            dp[j][j + i] = min(dp[j + 1][j + i - 1], dp[j][j + i - 2]) + 1
        else:
            for k in range(j, j + i):
                dp[j][j + i] = max(dp[j][j + i], dp[j][k] + dp[k + 1][j + i])
                
print(length - dp[0][length * 2 - 1])


    

    
    
    
    


            


    



