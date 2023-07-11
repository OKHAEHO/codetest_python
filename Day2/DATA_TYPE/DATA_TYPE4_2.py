#특정 인덱스에 데이터 추가

a = [1,4,3]
a.insert(2, 9) # 예상 : [1,4,9,3]
print(a) #희희 맞아따

print("값이 3인 데이터 개수 세기 : ", a.count(3))

a.remove(1) # 1인 값 삭제
print(a)

a = [1,2,3,4,5,5,5]
remove_set = {3,5} #특정 원소 모두 삭제 set로 묶어가지고 없애버린다 라고 생각하면 될 듯

result = [i for i in a if i not in remove_set]
print(result)