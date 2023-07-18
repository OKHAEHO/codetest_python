from bisect import bisect_left, bisect_right


array = []

n, value = map(int, input('원소와 횟수를 보고 싶은 숫자를 입력하세요: ').split(' '))

#print(n, x)

array = list(map(int, input('원소를 넣으세요 : ').split(' ')))


def count_by_value(array, value):
    left_index = bisect_left(array, value)
    right_index = bisect_right(array, value)
    return right_index - left_index  # 특정 값의 개수 반환

count = count_by_value(array, value)
print("특정 값의 개수는 {}입니다.".format(count))
