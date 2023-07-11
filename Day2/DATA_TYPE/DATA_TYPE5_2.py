#자료형
b = (2,'bakery','coffee',3.13,[5,4,3,2,1])

b = b + (1.3,'name',5)

print(b)

t_length = len(b)
print(t_length)
print(b)

lst = list(b)
lst.append('add') #튜플은 다양한 걸 사용하기 위해 쓰는건데 왜 list로 바꿔가지고 append를 사용하는가?
c = tuple(lst)    #튜플에서 append가 안먹음
print(c)

if 'coffee' in b :
    print("커피가 존재합니다.")
if '3.333' not in b :
    print('3.333은 존재하지 않습니다.')
    
d = (3,4444,(55,55),5)
print(d)