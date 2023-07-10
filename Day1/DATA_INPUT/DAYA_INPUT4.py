#Day1 - 입력과 출력
data = input("문자를 입력해주세요, 닷으로 구분 : ").split(",")
print("-".join(data))
data.reverse()
print(":".join(data))
print(data[0], data[1])