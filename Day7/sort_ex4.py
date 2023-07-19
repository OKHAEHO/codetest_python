from bisect import bisect_left, bisect_right


array = []

n, value = map(int, input('원소와 횟수를 보고 싶은 숫자를 입력하세요: ').split(' '))

#print(n, x)

array = list(map(int, input('원소를 넣으세요 : ').split(' ')))


def count_by_value(array, value):
    left_index = bisect_left(array, value) #왼쪽에서 value를 찾아서 인덱스 번호를 저장한다.
    right_index = bisect_right(array, value) #오른쪽에서 value를 찾아서 인덱스 번호를 저장한다.
    return right_index - left_index  # 특정 값의 개수 반환 ( 오른쪽에서 왼쪽에서 인덱스 번호를 뺴면 해당 value의 갯수를 알 수 있다.)

count = count_by_value(array, value)
print("특정 값의 개수는 {}입니다.".format(count))