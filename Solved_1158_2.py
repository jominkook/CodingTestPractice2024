N,K = map(int,input().split())

people = [i for i in range(1,N+1)]

idx = 0

print("<",end="")
while len(people) > 1:
    idx = (idx + K - 1) % len(people)
    print(people.pop(idx),end=", ")
    
print(people[0],end=">")