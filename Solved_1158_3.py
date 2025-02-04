#백준 1158 요세푸스 문제
# 3번째 풀이

N,K = map(int, input().split())

people = [i for i in range(1, N+1)]

result = []

idx = 0

while people:
    idx = (idx + K - 1) % len(people)
    result.append(people.pop(idx))
    
print('<', end = '')
print(*result, sep = ', ', end = '')
print('>')