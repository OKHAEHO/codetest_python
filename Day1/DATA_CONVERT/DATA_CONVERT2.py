#Day1 - 변환과 연산자 

s = input("반복할 문자열 입력 : ")
ss = int(input("반복할 횟수 : "))
print(s * ss)

a, b = input("단어를 여러번 출력 : ").split()
print(a * int(b))


a, b = map(int, input("정수 2개를 입력받아 차를 계산 : ").split()) # map을 활용해서 정수로만 입력 방식을 지정
print(a-b)

a, b = input('정수 2개를 입력 받아 차를 계산 : ').split() # 직접 정수 캐스팅
c = int(a)-int(b) # 빼기
d = int(a)*int(b) # 곱하기
e = int(a)//int(b) # 나누기
f = int(a)%int(b) # 나머지
print('차, 곱, 몫, 나머지 연산 결과 :', c, d, e, f) # 사칙 연산 출력

