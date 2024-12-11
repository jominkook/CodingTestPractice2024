import sys
input = sys.stdin.readline
text = input().strip()
M = int(input())

left = []
right = []

for _ in range(M):
    command = input().strip()
    if command[0] == 'L':
        if text:
            right.append(text[-1])
            text = text[:-1]
    elif command[0] == 'D':
        if right:
            text += right.pop()
    elif command[0] == 'B':
        if text:
            text = text[:-1]
    else:
        text += command[2]
        
print(text + ''.join(right[::-1]))