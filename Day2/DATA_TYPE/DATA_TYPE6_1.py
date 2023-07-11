#자료형
dic = dict()
dic['사과'] = 'Apple'
dic['바나나'] = 'Banana'
dic['코코넛'] = 'Coconut'
dic2 = {'a':123123, (1,1):654321, 1:'banana'}

print(dic)
print(dic2)
print(type(dic))

if '사과' in dic :
    print("'사과'를 키로 가지는 데이터가 존재합니다.")