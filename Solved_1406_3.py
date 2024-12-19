#에디터문제
#시간초과 발생!!

words = input()
N = int(input())

cursor = len(words)
for _ in range(N):
    command = input().split()
    if command[0] == 'L':
        if cursor > 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor < len(words):
            cursor += 1
    elif command[0] == 'B':
        if cursor > 0:
            words = words[:cursor-1] + words[cursor:]
            cursor -= 1
    elif command[0] == 'P':
        words = words[:cursor] + command[1] + words[cursor:]
        cursor += 1
        
print(words)