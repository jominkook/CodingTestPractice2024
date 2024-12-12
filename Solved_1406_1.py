import sys
sys.stdin.readline
text = sys.stdin.readline().strip()
M = int(sys.stdin.readline())

left = []
right = []

for i in range(len(text)):
    left.append(text[i])
    
for i in range(M):
    cmd = sys.stdin.readline().strip()
    if cmd[0] == 'L' and left:
        right.append(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.pop())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[2])
                
print(''.join(left + right[::-1]))