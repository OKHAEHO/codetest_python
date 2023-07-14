from itertools import combinations

S = input("숫자를 입력하세요: ")
X = int(input('제거할 숫자의 갯수를 입력하세요: '))

rm = int(len(S) - X)
S_list = list(S[:len(S)])

combinations = list(combinations(S_list, rm))

print(*max(combinations))
