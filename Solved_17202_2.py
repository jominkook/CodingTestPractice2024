num1 = input()
num2 = input()

dp = [0] * 16



for i in range(8):
    dp[i*2] = int(num1[i])
    dp[i*2+1] = int(num2[i])


while len(dp) > 2:
    for i in range(len(dp)-1):
        dp[i] = (dp[i] + dp[i+1]) % 10
    dp.pop()
    
print(''.join(map(str, dp)))
    

    

