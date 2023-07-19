#문제 : 전자매장에 부품이 N개가 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 
#내일 M개 종류의 부품을 대량으로 납품해야 한다. 매장 내에 모든 부품을 확인하는 프로그램을 작성하자.

array = []
array2 = []
goods = []

N = int(input('부품의 갯수를 입력하세요 : '))

array = list(map(int, input('부품의 종류를 넣으세요 : ').split(' ')))

M = int(input('손님이 찾는 부품을 입력하세요 : '))

target = list(map(int, input('부품의 종류를 넣으세요 : ').split(' ')))

array.sort()

print(array)
print(array2)

while True :
    for x in target :
        if x in array:
            goods.append("yes")
        else :
            goods.append("no")
    break
    
print(*goods)