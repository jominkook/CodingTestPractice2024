# 백준 문자열교환 1522번 문제
# 9번째 풀이과정

s = input()

a = s.count('a')

s = s + s

min_val = float('inf')

for i in range(len(s)):
    window = s[i:i+a]
    if len(window) < a:
        break
    min_val = min(min_val, window.count('b'))
    
print(min_val)