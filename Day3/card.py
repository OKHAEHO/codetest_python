import random

N = int(input("행의 개수를 입력하세요: "))
M = int(input("열의 개수를 입력하세요: "))

mini = []
array = [[0] * M for _ in range(N)]

#행렬만들기
for i in range (N) :
    for j in range (N) :
        array[i][j] = random.randint(1,10)


for row in array :
    
    mini.append(min(row))

total = max(mini)

print(array)
print(mini)


print(total)