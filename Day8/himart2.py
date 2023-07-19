from bisect import bisect_left, bisect_right

N = int(input('부품의 갯수를 입력하세요: '))
array = list(map(int, input('부품의 종류를 넣으세요: ').split(' ')))

M = int(input('손님이 찾는 부품을 입력하세요: '))
target = list(map(int, input('부품의 종류를 넣으세요: ').split(' ')))

result = []
array.sort()

def find(array, target):
    for value in target:
        left = bisect_left(array, value)
        right = bisect_right(array, value)
        if left != right:
            result.append('옥지얌 있어!!')
        else:
            result.append('옥지얌 없어ㅠㅠ')

find(array, target)
print(result)
