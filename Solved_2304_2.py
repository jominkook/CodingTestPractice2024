#2304 창고다각형 문제

N = int(input())

#기둥
h_list = []
highest = 0
h_idx = 0

for i in range(N):
    L,H = map(int,input().split())
    h_list.append([L,H])
    
    if H > highest:
        highest = H
        h_idx = i
        
h_list.sort()

area = 0

#왼 -> 기둥까지
# 첫높이
h = h_list[0][1]

for i in range(h_idx):
    # 다음 기둥의 높이가 지금것보다 높으면 다음 기둥까지만 더하면 됨(갱신 필요)
    if h < h_list[i+1][1]:
        area += h * (h_list[i+1][0] - h_list[i][0])
        
        #다음 기둥까지의 높이로 갱신
        h = h_list[i+1][1]
    else:
        area += h * (h_list[i+1][0] - h_list[i][0])
        
#오 -> 기둥까지
h = h_list[-1][1]

for i in range(N-1,h_idx,-1):
    #다음 기둥의 높이가 지금보다 높으면 다음 기둥까지만 더하면 됨(갱신 필요)
    if h < h_list[i-1][1]:
        area += h * (h_list[i][0] - h_list[i-1][0])
        h = h_list[i-1][1]
    else:
        area += h * (h_list[i][0] - h_list[i-1][0])
        
print(area)
