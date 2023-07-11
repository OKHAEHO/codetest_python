#자료형
a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[3])

#크기가 n이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
b = [0] * n
print(b)

print(a[-1])
print(a[-3])

a[3] = 7
print(a)
print(a[1:4])

array = [i for i in range(1, 10)]
print(array)

array = []
for i in range(10) :
    if i % 2 == 1:
        array.append(i)
print(array)