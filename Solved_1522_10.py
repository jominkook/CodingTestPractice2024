# 백준 1522 문자열 교환
# 윈도우 알고리즘
# 10번째 풀이

str = input()
A = str.count('a')
str = str + str

min_A = float('inf')

for i in range(len(str)//2):
    window = str[i:i+A]
    min_A = min(min_A, A - window.count('a'))
    
print(min_A)
    
    
    
  








    
        
        




    
    
    
    
        
    
        


