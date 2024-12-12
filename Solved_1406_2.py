#시간초과 코드

import sys
sys.stdin.readline

text = str(input())

cursor = len(text)
M = int(input())

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor != len(text):
            cursor += 1
    elif command[0] == 'B':
        if cursor != 0:
            text = text[:cursor-1] + text[cursor:]
            cursor -= 1
    elif command[0] == 'P':
        text = text[:cursor] + command[1] + text[cursor:]
        cursor += 1
        
print(text)