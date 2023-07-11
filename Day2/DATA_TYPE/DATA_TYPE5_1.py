#자료형
a = (1,2,3,4,5,6,7,8,9)
this_is_not_tuple = ("Seoul") #튜플이 뭐야?
print(type(this_is_not_tuple))

this_is_tuple = ("Seoul",) #튜플로 선언하려면 ,가 하나는 있어야한다.
print(type(this_is_tuple))

print(a[3])
print(a[1:4])
print(a[:]) #전체 리스트 보이기
print(type(a)) #튜플은 여러가지 데이터 타입을 섞어서 쓸 때 사용한다. 리스트는 동일한 데이터타입만 사용할 수 있다?

#a[1] = 'i'

b = (1,'apple', 'banana', 3.13, [1,2,3,4,5])

c = tuple(range(1,10))
print(b)

for c_tuple in c :
    print(c_tuple) #하나 찍고 엔터 하나 찍고 엔터 이런 식으로 데이터를 출력
    
print(c)