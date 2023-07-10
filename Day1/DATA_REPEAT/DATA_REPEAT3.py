#Day1 - 조건문, 반복문
n = int(input("정수 1개를 입력받아 분류하기 : "))
if n < 0 :
    if n % 2 == 0:
        print("음수, 짝수 : A")
    else : 
        print("음수, 홀수 : B")
else : 
    if n % 2 == 0 :
        print("양수 ,짝수 : C")
    else : 
        print("양수, 홀수 : D")