a = int(input('몇개를 넣을것이냐! : '))
x = 0
array = [int(input('숫자를 입력하세요 : ')) for _ in range(a)]

rever = sorted(array, reverse=True)

print(rever)

