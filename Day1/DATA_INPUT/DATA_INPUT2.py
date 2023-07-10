#Day1 - 입력과 출력

print("첫번 째 정수를 입력하세요 : ", end='')
a = input()
print("두번 째 정수를 입력하세요 : ", end='')
b = input()

print(a, b)
print(b ,a)

print("한번에 문자를 2번 입력받았습니다 : ",end='')
c,d = input().split() # 문자 2개를 입력, 공백 기준 분리, 정수형 map(int,input.split()), 실수형 map(float, input.split)

print(c, d)