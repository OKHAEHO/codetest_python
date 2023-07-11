#자료형
a = "Hello"
b = "World"
print(a + " " + b)

c = "String"
print(c * 3)

d = "ABCDEF"
print(d[2:4])
print(d[2:])
print(d[0])
print(d[:5])

str_length = len(d) #문자의 길이를 알아내는 귀여운 코드
print(str_length)

str_min = min(d) #문자열 중 가장 작은 값 호출
print(str_min) 

str_max = max(d) #문자열 중 가장 큰 값 호출
print(str_max)

str_count = d.count("B") #문자열 중 해당 글자의 갯수 (중요)
print(str_count)

print(d.find("C")) #문자열 중 해당 글자의 인덱스 번호 호출 (중요)

print(d.replace("C", "c")) #특정 문자을 해당 문자로 바꾸기 (중요)