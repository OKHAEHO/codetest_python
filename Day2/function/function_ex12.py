
a,b,c = map(int, input("3개의 숫자를 입력하세요. (1~5까지)").split())

from itertools import permutations
data=[a,b,c]
result = list(permutations(data, 3))
print(result)