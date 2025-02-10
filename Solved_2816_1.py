# 백준 2816 디지털티비
# 첫번째 풀이

N = int(input())

channels = []

for i in range(N):
    channels.append(input())
    
if channels[0] == 'KBS1':
    print('1'*i + '4'*i)
    print('4'*i + '1'*i)
elif channels[0] == 'KBS2':
    print('1'*i + '4'*i)
    print('4'*i + '1'*i)
else:
    for i in range(N):
        if channels[i] == 'KBS1':
            print('1'*i + '4'*i)
            print('4'*i + '1'*i)
            break
    for i in range(N):
        if channels[i] == 'KBS2':
            print('1'*i + '4'*i)
            print('4'*i + '1'*i)
            break
        
        
        
        
        
        
        
        
        



