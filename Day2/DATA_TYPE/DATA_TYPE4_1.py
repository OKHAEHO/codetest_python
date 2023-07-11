#자료형
n = 4
m = 3
array = [[0] * m for _ in range(n)] # array를 리스트로 만든다 [0]을 갯수만큼 그리고 [0,0,0]을 for문을 굴려서 갯수를 만든다
print(array)
print(type(array))

array[2][1] = 5 #예상 [0,0,0] [0,0,0] [0,5,0] [0,0,0] 
print(array) # 희희 맞았다~

a = [1,4,3]
print("기본 리스트 : ", a)

a.append(2) # 맨 뒤에 추가가 됨
print("insert : ", a)

a.sort() # 오름차순 정렬
print("오름차순 : " ,a)

a.sort(reverse = True)
print("내림차순 : ",a)