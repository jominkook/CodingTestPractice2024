#시간초과발생!!

words = str(input())
N = int(input())
cursor = len(words)

for i in range(N):
    cmd = input().split()
    if cmd[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif cmd[0] == 'D':
        if cursor != len(words):
            cursor += 1
    elif cmd[0] == 'B':
        if cursor != 0:
            words = words[:cursor-1] + words[cursor:]
            cursor -= 1
    elif cmd[0] == 'P':
        words = words[:cursor] + cmd[1] + words[cursor:]
        cursor += 1
print(words)
        