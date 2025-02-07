# 백준 20125 쿠키의 신체 측정
# 2번째 풀이

N = int(input())

cookie = [list(input()) for _ in range(N)]


def heart():
    for i in range(N):
        for j in range(N):
            if cookie[i][j] == '*':
                return i+2,j+1
            
            
def left(x,y):
    cnt = 0
    while y >= 0 and cookie[x][y] == '*':
        cnt += 1
        y -= 1
    return cnt


def right(x,y):
    cnt = 0
    while y < N and cookie[x][y] == '*':
        cnt += 1
        y += 1
    return cnt


def lower(x,y):
    cnt = 0
    while x < N and cookie[x][y] == '*':
        cnt += 1
        x += 1
    return cnt


heartX,heartY = heart()

x = heartX -1
y = heartY -1

waist = lower(x+1,y)

body = [left(x, y- 1),right(x,y+1),lower(x+1,y),lower(x+waist+1,y-1),lower(x+waist+1,y+1)]

print(heartX,heartY)
print(*body)



   





