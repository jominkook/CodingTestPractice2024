N = int(input())
q = [i for i in range(1, N+1)]
while len(q) > 1:
    q.pop(0)
    q.append(q.pop(0))   
print(q[0])