#자료형
dic3 = {'key':'문자열데이터 값',(3,3):654321, 999:'apple'} #데이터길ㄹ이가 왔다갔다하거나 수정이 잘 일어날 때 dic을 사용한다.

print(f'dic3["key"] = {dic3["key"]}')

print({dic3["key"]})
print({dic3[(3,3)]})

dic3["hello"]  = 2022
dic3[999] = 'banana'

del dic3["key"]
print(dic3)