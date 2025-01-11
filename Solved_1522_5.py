S = input().strip()
A = S.count('a')

# 문자열을 두 번 이어붙여 순환하는 효과를 줍니다.
S = S + S

min_val = float('inf')

# 슬라이딩 윈도우를 사용하여 최소 'b'의 개수를 찾습니다.
for i in range(len(S) // 2):
    window = S[i:i + A]
    min_val = min(min_val, window.count('b'))

print(min_val)